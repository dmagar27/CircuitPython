import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9)

r = 0
b = 0
g = 0

while True:
    try:
        sonarValue = sonar.distance
        print(sonarValue)
        if sonarValue < 5:
            dot.fill((225, 0, 0))
        if sonarValue > 35:
                dot.fill((0, 225, 0))
        if sonarValue <= 25 and sonarValue > 5:
            r = simpleio.map_range(sonarValue, 5, 20, 225, 0)
            b = simpleio.map_range(sonarValue, 5, 20, 0, 225)
            g = 0
        elif sonarValue > 20:
            r = 0
            b = simpleio.map_range(sonarValue, 20, 35, 225, 0)
            g = simpleio.map_range(sonarValue, 20, 35, 0, 225)
        dot.fill((int(r), int(g), int(b)))
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.1)