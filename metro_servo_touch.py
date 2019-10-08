import time
import board
import pulseio
import touchio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

angle = 5

while True:
    if touch_A1.value:
        print("Touched A1!")
        if angle < 180:
            angle = angle + 1
            my_servo.angle = angle


    if touch_A2.value:
        print("Touched A2!")
        if angle > 0:
            angle = angle - 1
            my_servo.angle = angle
    time.sleep(0.01)