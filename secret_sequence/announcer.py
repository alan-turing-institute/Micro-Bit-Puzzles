from microbit import *
import radio
import random

secret = "".join([random.choice("AB") for i in range(10)])

radio.on()

radio.send(secret)

for letter in secret:
    while True:
        display.show(letter)
        incoming = radio.receive()
        if incoming is None:
            continue
        elif incoming == letter:
            display.show(Image.YES)
            sleep(500)
            break
        else:
            display.show(Image.NO)
            sleep(500)

radio.send("complete")
display.show(Image.HEART)
