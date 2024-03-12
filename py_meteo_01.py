from sense_emu import SenseHat
import time

hat = SenseHat()
hat.clear()

temperature = hat.get_temperature()
temperature_from_humidity = hat.get_temperature_from_humidity()
temperature_from_pressure = hat.get_temperature_from_pressure()

print(f'Temperatura je: {round(temperature, 2)}° C')
print(f'Temperatura iz vlaznosti je: {round(temperature_from_humidity, 2)}° C')
print(f'Temperatura iz tlaka je: {round(temperature_from_pressure, 2)}° C')


