#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait
import time

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors and sensor.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.S2)  # Assume color sensor is connected to Port S2

# Define the target color sequence
TARGET_COLORS = [Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE]

# Constants
MOVE_TIMEOUT = 1500  # Time to move in one direction before switching (in ms)
DEBOUNCE_READINGS = 5  # Number of readings for debouncing
PAUSE_SECONDS = 2  # Pause duration after detecting a color
SPEED = 325  # Motor speed

def detect_color():
    """Debounce the color detection by taking multiple readings."""
    readings = []
    for _ in range(DEBOUNCE_READINGS):
        readings.append(color_sensor.color())
        wait(10)
    most_common_color = max(set(readings), key=readings.count)
    ev3.screen.print(most_common_color)  # Debugging statement to print detected color
    return most_common_color

def move_robot(speed, direction='forward'):
    """Move the robot in the specified direction."""
    if direction == 'forward':
        left_motor.run(speed)
        right_motor.run(speed)
    elif direction == 'backward':
        left_motor.run(-speed)
        right_motor.run(-speed)

def stop_robot():
    """Stop the robot."""
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

def search_color(target_color, speed, unlimited_time=False):
    """Move forward or backward to find the target color."""
    found = False

    if unlimited_time:
        move_robot(speed)
        while not found:
            if detect_color() == target_color:
                stop_robot()
                pause_and_wait(PAUSE_SECONDS)
                found = True
            wait(10)
        return

    # Move forward first with a timeout
    move_robot(speed)
    start_time = time.time()
    while not found and (time.time() - start_time) < MOVE_TIMEOUT / 1000:
        if detect_color() == target_color:
            stop_robot()
            pause_and_wait(PAUSE_SECONDS)
            found = True
        wait(10)
    
    # If not found in the forward direction, move backward for twice as long
    if not found:
        move_robot(speed, direction='backward')
        start_time = time.time()
        while not found and (time.time() - start_time) < (2 * MOVE_TIMEOUT) / 1000:
            if detect_color() == target_color:
                stop_robot()
                pause_and_wait(PAUSE_SECONDS)
                found = True
            wait(10)

def pause_and_wait(seconds):
    """Pause for a specified number of seconds."""
    wait(seconds * 1000)  # Convert seconds to milliseconds

try:
    current_target_index = 0

    # First, search for the red color with no time limit
    search_color(TARGET_COLORS[current_target_index], SPEED, unlimited_time=True)
    current_target_index += 1

    # Main loop to move through the remaining target colors with a timeout
    while current_target_index < len(TARGET_COLORS):
        search_color(TARGET_COLORS[current_target_index], SPEED)
        current_target_index += 1

except KeyboardInterrupt:
    stop_robot()
