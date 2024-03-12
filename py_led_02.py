from sense_emu import SenseHat
import time

hat = SenseHat()

text_colour = [255, 0, 0]
background = [0, 0, 0]
msg = 'Pozdrav'

for letter in msg:
    hat.show_letter(letter,
                text_colour=text_colour,
                back_colour=background)
    time.sleep(0.5)