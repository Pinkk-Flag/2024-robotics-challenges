#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Function to move in a circle.
def move_in_circle(left_speed, right_speed, rotations):
    # Reset the motor encoders
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    # Define the target rotations
    target_left_angle = rotations * 360  # Convert rotations to degrees
    target_right_angle = rotations * 360  # Convert rotations to degrees
    
    # Run the motors
    left_motor.run(left_speed)
    right_motor.run(right_speed)
    
    # Wait until the motors have completed the target rotations
    while abs(left_motor.angle()) < target_left_angle and abs(right_motor.angle()) < target_right_angle:
        wait(10)  # Wait a short period before checking again
    
    # Stop the motors
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)

try:
    # Main loop to create a figure-8 pattern indefinitely.

    # First circle (right motor faster, left motor slower)
    move_in_circle(left_speed=100, right_speed=400, rotations=5.33)  # 6.5 rotations
    
    # Short pause to ensure smooth transition
    wait(500)  # 500 ms pause
    
    # Second circle (left motor faster, right motor slower)
    move_in_circle(left_speed=400, right_speed=100, rotations=5.33)  # 6.5 rotations
    
    # Short pause to ensure smooth transition
    wait(500)  # 500 ms pause

    # Optional: Sound the speaker to indicate a new figure-8 loop
    ev3.speaker.beep()
except KeyboardInterrupt:
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
