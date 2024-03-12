from sense_emu import SenseHat
import time

hat = SenseHat()

r = [255, 0, 0]
g = [0, 255, 0]
b = [0, 0, 255]
w = [255, 255, 255]

up = [b, b, b, b, b, b, b, b,
    b, b, b, g, g, b, b, b,
    b, b, g, b, b, g, b, b,
    b, g, b, b, b, b, g, b,
    g, b, b, b, b, b, b, g,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
        ]


while True:
    base_temp = round(hat.get_temperature(), 1)
    time.sleep(0.2)
    current_temp = round(hat.get_temperature(), 1)
    if base_temp > round(hat.get_temperature(), 1):
        hat.set_rotation(180)
        hat.set_pixels(pixel_list=up)
    else:
        hat.set_rotation(0)
        hat.set_pixels(pixel_list=up)