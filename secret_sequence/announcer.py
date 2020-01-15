from microbit import *
import radio

secret = "ABBABABA"

radio.on()

for letter in secret:
    while True:
        display.show(letter)
        incoming = radio.receive()
        if incoming is None:
            continue
        elif incoming == letter:
            display.show(Image.YES)
            sleep(1000)
            break
        else:
            display.show(Image.NO)
            sleep(1000)

display.show(Image.HEART)
