#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Function to move in a circle.
def move_in_circle(left_speed, right_speed, duration):
    left_motor.run(left_speed)
    right_motor.run(right_speed)
    wait(duration)
    left_motor.stop()
    right_motor.stop()
try:
    # Main loop to create a figure-8 pattern indefinitely.
    while True:
        # First circle (left motor slower, right motor faster)
        move_in_circle(left_speed=400, right_speed=800, duration=6000)  # Adjust speeds and duration as necessary
        
        # Second circle (right motor slower, left motor faster)
        move_in_circle(left_speed=800, right_speed=400, duration=6000)  # Adjust speeds and duration as necessary

        # Wait a moment before the next figure-8
        wait(500)
except KeyboardInterrupt:
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)