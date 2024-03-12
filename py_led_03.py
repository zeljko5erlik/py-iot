from sense_emu import SenseHat
import time

hat = SenseHat()
hat.clear()
time.sleep(0.7)
hat.set_pixel(5, 3, 255,0,0)
time.sleep(0.7)
hat.set_pixel(3, 3, 255,0,0)
time.sleep(0.7)
hat.set_pixel(1, 3, 255,0,0)

hat.clear()
r = [255, 0, 0]
g = [0, 255, 0]
b = [0, 0, 255]
w = [255, 255, 255]

hat.clear()
flag = [
    r, r, w, w, r, r, w, w,
    r, r, w, w, r, r, w, w,
    w, w, r, r, w, w, r, r,
    w, w, r, r, w, w, r, r,
    r, r, w, w, r, r, w, w,
    r, r, w, w, r, r, w, w,
    w, w, r, r, w, w, r, r,
    w, w, r, r, w, w, r, r,
]

hat.set_pixels(pixel_list=flag)
time.sleep(2)

hat.set_rotation(r=90)
angles = [0, 90, 180, 270, 0]

for angle in angles:
    hat.set_rotation(angle)
    time.sleep(1)

while True:
    hat.set_rotation(0)
    time.sleep(1)
    hat.set_rotation(90)
    time.sleep(1)



