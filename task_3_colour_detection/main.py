#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors and sensor.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.S1)  # Assume color sensor is connected to Port S1

# Define color detection thresholds
COLOR_THRESHOLDS = {
    Color.RED: 10,
    Color.GREEN: 10,
    Color.YELLOW: 10,
    Color.BLUE: 10
}

def detect_color():
    """Detect the color of the marker."""
    color = color_sensor.color()
    return color

def move_to_color(target_color, speed):
    """Move the robot forward until the target color is detected."""
    left_motor.run(speed)
    right_motor.run(speed)
    
    while detect_color() != target_color:
        wait(10)  # Small delay to prevent rapid checking
    
    # Stop the robot when the color is detected
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

def pause_and_wait(seconds):
    """Pause for a specified number of seconds."""
    wait(seconds * 1000)  # Convert seconds to milliseconds

try:
    # Move to red, pause, then yellow, green, blue
    move_to_color(Color.RED, 500)  # Move to red marker
    pause_and_wait(2)              # Pause for 2 seconds

    move_to_color(Color.YELLOW, 500)  # Move to yellow marker
    pause_and_wait(2)                # Pause for 2 seconds

    move_to_color(Color.GREEN, 500)   # Move to green marker
    pause_and_wait(2)                # Pause for 2 seconds

    move_to_color(Color.BLUE, 500)    # Move to blue marker
    pause_and_wait(2)                # Pause for 2 seconds

    # Move back to follow the real-life order
    left_motor.run(-500)  # Reverse direction
    right_motor.run(-500)
    wait(4000)  # Adjust time to ensure it moves back to the starting position
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

except KeyboardInterrupt:
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
