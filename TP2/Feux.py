from microbit import *

#Turn off display to use gpio on extension board
display.off()

while True:
    pin8.write_digital(1) #red led on
    sleep(2000)
    pin8.write_digital(0) #red led off
    pin7.write_digital(1) #green led on
    sleep(2000)
    pin7.write_digital(0) #green led off
    pin6.write_digital(1) #orange led on
    sleep(1000)
    pin6.write_digital(0) #orange led off