import pico_4wd as car
import time
"""
def test_motor():
    speed = 50
    act_list = [
        "forward",
        "backward",
        "left",
        "right",
        "stop",
    ]
    print("Hello")
    for act in act_list:
        print(act)
        car.move(act, speed)
        time.sleep(1)

def test_sonar():
    now = time.time()
    end_loop = time.time() + 10
    while now < end_loop:
        now = time.time()
        distance = car.sonar.get_distance()
        print("distance:{}".format(distance))
        time.sleep(1)

def test_servo():
    for angle in range(0, 90):
        print("angle:%s "%angle)
        car.servo.set_angle(angle)
        time.sleep(0.005)
    for angle in range(90, -90, -1):
        print("angle:%s "%angle)
        car.servo.set_angle(angle)
        time.sleep(0.005)
    for angle in range(-90, 0):
        print("angle:%s "%angle)
        car.servo.set_angle(angle)
        time.sleep(0.005)

def test_light():
    print("red")
    for i in range(24):
        car.set_light_color_at(i, [255, 0, 0])
        time.sleep(0.01)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
        time.sleep(0.01)
    print("green")
    for i in range(24):
        car.set_light_color_at(i, [0, 255, 0])
        time.sleep(0.01)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
        time.sleep(0.01)
    print("blue")
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 255])
        time.sleep(0.01)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
        time.sleep(0.01)
    print("white")
    for i in range(24):
        car.set_light_color_at(i, [255, 255, 255])
        time.sleep(0.01)
    for i in range(24):
        car.set_light_color_at(i, [0, 0, 0])
        time.sleep(0.01)

def set_light():
    for i in range(24):
        car.set_light_color_at(i, [255, 255, 255])
"""

def test_grayscale():
    """The REAL expected grayscale values are as follows:
       white ground > 20,000
       black ground > 7,000
       cliff < 7,000
    """
    #now = time.time()
    #end_loop = time.time() + 10
    #while now < end_loop:
    while True:
        now = time.time()
        grayValue = car.get_grayscale_values()
        print('left:%d, middle:%d, right:%d' %(grayValue[0], grayValue[1], grayValue[2]))
        time.sleep(1)

"""
def test_speed():
    def helper(power):

        power = round(power / 10) * 10
        car.move("forward", power)
        print('Power(%%):%d Speed(cm/s):%.2f' % (power, car.speed()))
        time.sleep(0.2)

    # don't add a while loop here like a retard
    now = time.time()
    for power in range(100):
        helper(power)

    for power in range(100, -100, -1):
        helper(power)

    for power in range(-100, 0):
        helper(power)
"""
try:
    #test_motor()
    #test_sonar()
    #test_servo()
    #test_light()
    #set_light()
    test_grayscale()
    #test_speed()
finally:
    car.move("stop")
    car.set_light_off()
