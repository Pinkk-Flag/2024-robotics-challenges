#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

# Initialize the EV3 brick
ev3 = EV3Brick()

# Initialize motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Initialize ultrasonic sensor
us = UltrasonicSensor(Port.S1)

# Function to turn 90 degrees
def turn_90_degrees():
    # Stop motors before turning
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
    
    # Turn left 90 degrees
    left_motor.run_angle(500, -180)
    right_motor.run_angle(500, 180)
    # Alternatively, adjust speed and angle as per your robot's configuration

# Main loop
try:
    while True:
        # Get distance from ultrasonic sensor
        distance = us.distance()

        # Check if distance is greater than 10 cm
        if distance > 100:  # Distance is measured in millimeters
            turn_90_degrees()
            ev3.speaker.beep()
        else:
            # Move forward
            left_motor.run(500)
            right_motor.run(500)
        
        # Wait for a short time before checking again
        wait(100)  # Wait 100 ms

except KeyboardInterrupt:
    # Stop the motors when the program is interrupted
    left_motor.stop(Stop.BRAKE)
    right_motor.stop(Stop.BRAKE)
