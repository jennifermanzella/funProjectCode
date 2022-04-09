from pico_rdp import Motor, Speed, Servo, Ultrasonic, WS2812, mapping
from machine import Pin, ADC
import time

left_front  = Motor(17, 16, dir=1) # motor 1
right_front = Motor(15, 14, dir=-1) # motor 2
left_rear   = Motor(13, 12, dir=1) # motor 3
right_rear  = Motor(11, 10, dir=-1) # motor 4
motors = [left_front, right_front, left_rear, right_rear]

def motor_test(this_motor, seconds=10, power=10):
    this_motor.power = power
    time.sleep(seconds)
    this_motor.power = 0

motor_test(left_front, 10, 70)
motor_test(right_front, 10, 70)
motor_test(left_rear, 10, 70)
motor_test(right_rear, 10, 70)

# set power 
