from sense_emu import SenseHat
import time

hat = SenseHat()
hat.clear()

def get_led_matrix_picture(humidity):
    led_matrix = []
    color_down = [0, 0, 0]
    g = [0, 255, 0]
    y = [255, 255, 0]
    r = [255, 0, 0]
    if humidity < 45:
        color_up = g
    elif humidity > 45 and humidity < 75:
        color_up = y
    else:
        color_up = r

    for i in range(64):
        if i < int((64/100) * humidity):
            led_matrix.append(color_up)
        else:
            led_matrix.append(color_down)

    return led_matrix


while True:
    humidity = round(hat.get_humidity(), 2)
    led_matrix = get_led_matrix_picture(humidity)
    hat.set_pixels(pixel_list=led_matrix)
    time.sleep(1)
