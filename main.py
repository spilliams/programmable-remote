"""Hello, World"""
import board
import digitalio
import rotaryio
import time

import adafruit_ssd1681
import displayio
import busio
from fourwire import FourWire

ledBoard = digitalio.DigitalInOut(board.LED)
ledRed = digitalio.DigitalInOut(board.GP17)
ledGreen = digitalio.DigitalInOut(board.GP16)
for led in [ledBoard, ledRed, ledGreen]:
    led.direction = digitalio.Direction.OUTPUT

# rotary breakout COM is set to GND (so the encoder works), so pull gpio up to read a button presses as "on"

encoder = rotaryio.IncrementalEncoder(board.GP28, board.GP27)
last_position = 0

buttonCenter = digitalio.DigitalInOut(board.GP26) # "SW1" on rotary breakout
buttonDown = digitalio.DigitalInOut(board.GP22) # "SW2"
buttonRight = digitalio.DigitalInOut(board.GP21) # "SW3"
buttonUp = digitalio.DigitalInOut(board.GP20) # "SW4"
buttonLeft = digitalio.DigitalInOut(board.GP19) # "SW5"
for button in [buttonCenter, buttonDown, buttonRight, buttonUp, buttonLeft]:
    button.switch_to_input(pull=digitalio.Pull.UP)

# e-paper display pins
# epd_sck = digitalio.DigitalInOut(board.GP14)
# epd_miso = digitalio.DigitalInOut(board.GP12)
# epd_mosi = digitalio.DigitalInOut(board.GP15)
epd_ecs = digitalio.DigitalInOut(board.GP13)
epd_dc = digitalio.DigitalInOut(board.GP7)
# epd_srcs = digitalio.DigitalInOut(board.GP6)
# epd_sdcs = digitalio.DigitalInOut(board.GP5)
epd_reset = digitalio.DigitalInOut(board.GP4)
epd_busy = digitalio.DigitalInOut(board.GP3)
# epd_enable = digitalio.DigitalInOut(board.GP2)

displayio.release_displays()
spi = busio.SPI(clock=board.GP14, MOSI=board.GP15, MISO=board.GP12) # TypeError: command must be of type Pin, not DigitalInOut
display_bus = FourWire(
    spi, command=epd_dc, chip_select=epd_ecs, reset=epd_reset, baudrate=1000000
)
time.sleep(1)

display = adafruit_ssd1681.SSD1681(
    display_bus,
    width=200,
    height=200,
    busy_pin=epd_busy,
    highlight_color=0xFF0000,
    rotation=180,
)

g = displayio.Group()

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
