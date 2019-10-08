import board
import pulseio


class RGB(object):

    full = 65535

    def __init__(self, R, G, B):
        self.R = pulseio.PWMOut(R, frequency=5000, duty_cycle=0)
        self.G = pulseio.PWMOut(G, frequency=5000, duty_cycle=0)
        self.B = pulseio.PWMOut(B, frequency=5000, duty_cycle=0)

    def red(self):
        print("red")
        self.R.duty_cycle = 0
        self.G.duty_cycle = self.full
        self.B.duty_cycle = self.full

    def green(self):
        print("green")
        self.R.duty_cycle = self.full
        self.G.duty_cycle = 0
        self.B.duty_cycle = self.full

    def blue(self):
        print("blue")
        self.R.duty_cycle = self.full
        self.G.duty_cycle = self.full
        self.B.duty_cycle = 0

    def cyan(self):
        print("cyan")
        self.R.duty_cycle = self.full
        self.G.duty_cycle = 0
        self.B.duty_cycle = 0

    def magenta(self):
        print("magenta")
        self.R.duty_cycle = 0
        self.G.duty_cycle = self.full
        self.B.duty_cycle = 0

    def yellow(self):
        print("yellow")
        self.R.duty_cycle = 0
        self.G.duty_cycle = 0
        self.B.duty_cycle = self.full