#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor, Motor
from pybricks.parameters import Port
from pybricks.tools import wait
import math

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize sensors
us_left = UltrasonicSensor(Port.S1)
us_right = UltrasonicSensor(Port.S2)

# Initialize motors
motor_left = Motor(Port.A)
motor_right = Motor(Port.D)

# Configuration constants
DISTANCE_BETWEEN_SENSORS = 7.0  # in centimeters
THRESHOLD_DISTANCE = 15.0  # in centimeters
ANGLE_BUFFER = 5.0  # in degrees
FORWARD_SPEED = 250  # speed of the motors when moving forward
TURN_SPEED = 125  # speed adjustment for turning

while True:
    # Read distances from the ultrasonic sensors
    distance_left = us_left.distance() / 10  # Convert mm to cm
    distance_right = us_right.distance() / 10  # Convert mm to cm

    # Calculate the angle
    delta_d = distance_right - distance_left
    theta = math.atan2(delta_d, DISTANCE_BETWEEN_SENSORS) * 180 / math.pi

    # Adjust steering based on angle
    if distance_left < THRESHOLD_DISTANCE or distance_right < THRESHOLD_DISTANCE:
        if abs(theta) < ANGLE_BUFFER:
            # Move forward if the angle is within the buffer
            motor_left.run(FORWARD_SPEED)
            motor_right.run(FORWARD_SPEED)
        else:
            # Reverse the steering logic
            if theta > 0:
                # Turn left
                motor_left.run(FORWARD_SPEED - TURN_SPEED)
                motor_right.run(FORWARD_SPEED)
            else:
                # Turn right
                motor_left.run(FORWARD_SPEED)
                motor_right.run(FORWARD_SPEED - TURN_SPEED)
    else:
        # Stop if no object is detected within the threshold distance
        motor_left.stop()
        motor_right.stop()

    # Optional delay to avoid too rapid checking
    wait(100)
