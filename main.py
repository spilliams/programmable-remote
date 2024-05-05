"""Hello, World"""
import board
import digitalio
import time

red = digitalio.DigitalInOut(board.GP14)
green = digitalio.DigitalInOut(board.GP15)
red.direction = digitalio.Direction.OUTPUT
green.direction = digitalio.Direction.OUTPUT

while True:
    red.value = False
    green.value = True
    time.sleep(0.5)
    red.value = True
    green.value = False
    time.sleep(0.5)
