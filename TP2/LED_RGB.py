from microbit import *
from neopixel import NeoPixel

num_pixels = 8

led = NeoPixel(pin0, num_pixels)

while True:
    for i in range(0, num_pixels):
        led[i] = (0,0,255)     # set pixel i to red
        led.show()              # actually display it
        sleep(250)                # milliseconds

    for i in range(0, num_pixels):
        led[i] = (255,255,255)     # set pixel i to red
        led.show()              # actually display it
        sleep(250)                # milliseconds

    for i in range(0, num_pixels):
        led[i] = (255,0,0)     # set pixel i to red
        led.show()              # actually display it
        sleep(250)                # milliseconds