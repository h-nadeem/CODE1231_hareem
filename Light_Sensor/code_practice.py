# Simple Blinking LEDS
# This example makes your onboard lEDs blink!
# This example makes your onboard lEDs blink!
import time
import board
import board
import digitalio
led = digitalio.DigitalInOut(board.D13) # Onboard LED
led.direction = digitalio.Direction.OUTPUT
while True:
 led.value = True # Turn on the LED
 time.sleep(1) # Wait for 1 second
 led.value = False # Turn off the LED
 time.sleep(1) # Wait for 1 second