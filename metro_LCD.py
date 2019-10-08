from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
import board
import digitalio
import time


# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=4, num_cols=20)


lcd.clear()

# start at the second line, fifth column (numbering from zero).
lcd.set_cursor_pos(0, 0)
lcd.print("Switch State:")

# Make the cursor visible as a line.

button_a = digitalio.DigitalInOut(board.D2)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

counter = 0
while True:
    if button_a.value:
        counter += 1
        lcd.set_cursor_pos(1, 4)
        lcd.print(str(counter))
        time.sleep(0.1)
    else:
        counter = counter
        time.sleep(0.1)