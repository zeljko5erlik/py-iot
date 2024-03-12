# 1. korak import SenseHAT emulator modula
from sense_emu import SenseHat

# 2. korak - kreiranje SenseHAT emulator objekta

sens_hat = SenseHat()

# boja se definira kao RGB (red, green, blue) od 0 do 255

text_colour = [76, 139, 245]
background = [0, 0, 0]

while True:
    sens_hat.show_message('Hello, world!', 
                        scroll_speed=.2,
                        text_colour=text_colour,
                        back_colour=background)




