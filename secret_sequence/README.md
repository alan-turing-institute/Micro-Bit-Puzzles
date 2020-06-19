# Secret Sequence

A puzzle for two people. One Micro:Bits LED array shows a sequence of button
pressed, for example "A B B B A B A". This sequence must be entered on a second
Micro:Bit to solve the puzzle.

The Micro:Bit displaying the sequence can advance when it receives a radio
message from the other signalling that the correct button has been pressed.

Hopefully the magnetometer and/or accelerometer can be used to ensure the
Micro:Bits are being held "back-to-back" so that the solvers cannot see each
other's LED array.

## Items Required

- 2 x Micro:Bit

## Setup

- Convert each of the announcer and solver python files to hex
- Flash one of each hex to a Micro:Bit

### Using [uflash](https://github.com/ntoll/uflash)

```
pip install uflash
uflash announcer.py
```
swap Micro:Bits
```
uflash solver.py
```
