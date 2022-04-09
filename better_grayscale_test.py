import pico_4wd as car
import time

EXPECTING = "Detecting {}\n"

def test_grayscale():
    """The REAL expected grayscale values are as follows:
       white ground > 20,000
       black ground > 7,000
       cliff < 7,000
    """
    now = time.time()
    end_loop = time.time() + 360
    while now < end_loop:
        now = time.time()
        grayValue = car.get_grayscale_values()
        
        left_value = grayValue[0]
        middle_value = grayValue[1]
        right_value = grayValue[2]
        print("left:{}, middle:{}, right:{}".format(left_value, middle_value, right_value))
        average = (left_value + middle_value + right_value) / 3.0
        if average > 20000:
            print(EXPECTING.format("white"))
        elif average >7000:
            print(EXPECTING.format("black"))
        else:
            print(EXPECTING.format("cliff"))
        time.sleep(1)

try:
    test_grayscale()
finally:
    car.move("stop")
    car.set_light_off()
