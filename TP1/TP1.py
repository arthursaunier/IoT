from microbit import *

#EX 4

#while True:
#    if button_a.is_pressed():
#        display.show(Image.HAPPY)
#    if button_b.is_pressed():
#        display.show(Image.SAD)

#EX 5

#while True:
#    if (temperature() > 30):
#        display.show(Image.PACMAN)

#EX 6

#count = 0

#while True:
#    if accelerometer.was_gesture('left'):
#        count = count + 1
#        display.show(count)

#EX 7

compass.calibrate()

while True:

    bearing = compass.heading()
    if bearing < 45 or bearing > 315:
        display.show(Image.ARROW_N)
    else:
        display.show(' ')