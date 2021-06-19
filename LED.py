import board
import neopixel
import time
import random
import math


PIXEL_COUNT = 120
BRIGHTNESS = 0.01
PIXEL_BAND = 10
PIXELS_COUNTED = 0

BRIGHTNESS_DELAY = 2 # Seconds
BRIGHTNESS_STEP = 0.01
RANGE = 5

pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, brightness=BRIGHTNESS, pixel_order=neopixel.GRB)

class Led:

  def init():
    self.IS_RUNNING = False

  def startShow(self):
    #try:

      BRIGHTNESS = 0.01

      self.IS_RUNNING = True

      print('Show Starting')

      for c in range(math.floor(PIXEL_COUNT/PIXEL_BAND)):
        # Color
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)

        for b in range(RANGE):
          BRIGHTNESS = (BRIGHTNESS + BRIGHTNESS_STEP)
          pixels.brightness = BRIGHTNESS

          time.sleep(BRIGHTNESS_DELAY)

        for b in range(RANGE):
          pixels.brightness = 0
          time.sleep(0.1)
          pixels.brightness = BRIGHTNESS
          time.sleep(0.1)


        while self.IS_RUNNING == True:
          pixels.brightness = 0
          time.sleep(0.05)
          pixels.brightness = BRIGHTNESS
          time.sleep(0.05)

  def stopShow(self):
    self.IS_RUNNING = False
    pixels.brightness = 0
    BRIGHTNESS = 0.01
    print('Show Stopped')
    return True
