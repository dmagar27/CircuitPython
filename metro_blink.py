# Write your code here :-)
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D5)
led.direction = digitalio.Direction.OUTPUT


while True:
    led.value = True
    time.sleep(0.4)
    led.value = False
    time.sleep(0.4)