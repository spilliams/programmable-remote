"""Hello, World"""
import board
import digitalio
import rotaryio
import time

ledBoard = digitalio.DigitalInOut(board.LED)
ledRed = digitalio.DigitalInOut(board.GP6)
ledGreen = digitalio.DigitalInOut(board.GP5)
for led in [ledBoard, ledRed, ledGreen]:
    led.direction = digitalio.Direction.OUTPUT

# rotary breakout COM is set to GND (so the encoder works), so pull gpio up to read a button presses as "on"

encoder = rotaryio.IncrementalEncoder(board.GP13, board.GP12)
last_position = 0

buttonCenter = digitalio.DigitalInOut(board.GP11) # "SW1" on rotary breakout
buttonDown = digitalio.DigitalInOut(board.GP10) # "SW2"
buttonRight = digitalio.DigitalInOut(board.GP9) # "SW3"
buttonUp = digitalio.DigitalInOut(board.GP15) # "SW4"
buttonLeft = digitalio.DigitalInOut(board.GP14) # "SW5"
for button in [buttonCenter, buttonDown, buttonRight, buttonUp, buttonLeft]:
    button.switch_to_input(pull=digitalio.Pull.UP)


while True:
    ledBoard.value = not (buttonCenter.value and buttonDown.value and buttonRight.value and buttonUp.value and buttonLeft.value)
    
    position = encoder.position
    if last_position is None or position != last_position:
        print("Position: {}".format(position))
        ledGreen.value = position > last_position
        ledRed.value = position < last_position
        last_position = position
    else:
        ledGreen.value = False
        ledRed.value = False
    
    time.sleep(0.01)
