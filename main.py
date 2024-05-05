"""Hello, World"""
import board
import digitalio
# import rotaryio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# rotary breakout COM is set to 3V3, so pull gpio down to read a button presses as "on"

# encA = digitalio.DigitalInOut(board.GP14)
# encB = digitalio.DigitalInOut(board.GP15)
# encoder = rotaryio.InrementalEncoder(encA, encB)
# last_position = None

buttonCenter = digitalio.DigitalInOut(board.GP20) # "SW1" on rotary breakout
buttonDown = digitalio.DigitalInOut(board.GP19) # "SW2"
buttonRight = digitalio.DigitalInOut(board.GP18) # "SW3"
buttonUp = digitalio.DigitalInOut(board.GP17) # "SW4"
buttonLeft = digitalio.DigitalInOut(board.GP16) # "SW5"
buttons = [buttonCenter, buttonDown, buttonRight, buttonUp, buttonLeft]
for button in buttons:
    button.switch_to_input(pull=digitalio.Pull.DOWN)


while True:
    led.value = buttonCenter.value or buttonUp.value or buttonDown.value or buttonLeft.value or buttonRight.value
    time.sleep(0.1)
