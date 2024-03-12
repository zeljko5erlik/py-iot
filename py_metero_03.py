from sense_emu import SenseHat
import time

hat = SenseHat()
hat.clear()

def get_led_matrix_picture(color_up, color_down, humidity):
    led_matrix = []

    for i in range(64):
        if i < int((64/100) * humidity):
            led_matrix.append(color_up)
        else:
            led_matrix.append(color_down)

    return led_matrix

b = [0, 0, 0]
w = [255, 255, 255]

while True:
    humidity = round(hat.get_humidity(), 2)
    led_matrix = get_led_matrix_picture(w, b, humidity)
    hat.set_pixels(pixel_list=led_matrix)
    time.sleep(1)
