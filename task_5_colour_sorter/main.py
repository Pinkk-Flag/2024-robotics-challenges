#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Create your objects here.
ev3 = EV3Brick()

# Initialize the motor connected to port D (bucket motor).
motor_d = Motor(Port.D)

# Initialize the motor connected to port C (piston motor).
motor_b = Motor(Port.B)

# Initialize the color sensor connected to port 2.
color_sensor = ColorSensor(Port.S2)

# Define the positions for each color bucket (in degrees).
color_positions = {
    Color.RED: 0,
    Color.YELLOW: 90,
    Color.GREEN: 180,
    Color.BLUE: 270,
}

# Standby position (back to the starting position).
standby_position = 0

# Define piston movement in degrees.
piston_degrees = 90

# Adjust motor speed and wait times for slower operation.
motor_speed = 25  # Reduced speed
piston_wait_time = 3000  # Wait time for piston movement in milliseconds
bucket_wait_time = 3000  # Wait time for bucket movement in milliseconds
return_wait_time = 3000  # Wait time for the piston to return to initial position

def sort_color():
    # Detect the color.
    detected_color = color_sensor.color()

    if detected_color in color_positions:
        # Rotate the bucket motor to the correct position.
        motor_d.run_target(motor_speed, color_positions[detected_color])
        wait(bucket_wait_time)  # Wait for bucket motor to reach position

        # Move the piston 45 degrees to push the item into the bucket.
        motor_b.run_target(motor_speed, piston_degrees)
        wait(piston_wait_time)  # Allow time for the piston to move

        # Return the piston to its initial position.
        motor_b.run_target(motor_speed, 0)
        wait(return_wait_time)  # Allow time for the piston to return

        # Move the bucket motor back to the standby position.
        motor_d.run_target(motor_speed, standby_position)
        wait(bucket_wait_time)  # Wait for bucket motor to return to standby position

        # Stop the motors.
        motor_d.stop()
        motor_b.stop()

    else:
        # If the color is not recognized, beep as a warning.
        ev3.speaker.beep()

# Main loop to continuously check for colors.
while True:
    sort_color()
    wait(2000)  # Adjust the wait time between color checks as necessary.
