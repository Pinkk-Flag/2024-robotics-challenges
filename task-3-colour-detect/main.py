#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialise the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
tank = MoveTank(OUTPUT_A, OUTPUT_D)

# Initilise ultrasonic sensor 
us = UltrasonicSensor(INPUT_1)

# Initialise color sensor
color_sensor = ColorSensor(Port.S3)

task_index = 0
colours_needed = [Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE]




# ! TODO: BUILD THE ACTUAL ROBOT AND THEN FILL IN THE PROPER COLOUR SENSOR PORT!




# ================================================
# ================================================
# ================================================

def turn_90_degrees():
    tank.stop()
    tank.on_for_degrees(left_speed=50, right_speed=-50, degrees=180)

def lawn_mower_move():
    pass 
# ! TODO: FINISH THIS ALGORITHM ^^^^^^^^^^^^^


def identify_colour():
    detected_color = color_sensor.color()
    if detected_color == Color.RED:
        return "Red"
    elif detected_color == Color.GREEN:
        return "Green"
    elif detected_color == Color.BLUE:
        return "Blue"
    elif detected_color == Color.YELLOW:
        return "Yellow"
    else:
        return "Unknown"

try:
    while true:
        distance_to_ground = us.distance_cm

        if distance_to_ground > 10:
            turn_90_degrees()
            brick.sound.beep()
        else:
            tank.on(left_speed=50,right_speed=50)

        time.sleep(.01)


except KeyboardInterrupt:
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)