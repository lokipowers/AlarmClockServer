import board
import neopixel
import time
import random
import math
#import configparser
from db import *


PIXELS = 120
BRIGHTNESS = 0.01

pixels = neopixel.NeoPixel(board.D18, PIXELS, brightness=BRIGHTNESS, pixel_order=neopixel.GRB)


PIXEL_BAND = 10

PIXELS_COUNTED = 0


#BRIGHTNESS_TRANSITION = 100 # Microseconds
BRIGHTNESS_DELAY = 2 # Seconds
BRIGHTNESS_STEP = 0.1
RANGE = 10

#config = configparser.ConfigParser()

def shouldStop():
  #config.read("config.txt")
  #IS_RUNNING = config.getboolean("config", "isRunning")
  cursor = db.cursor()
  cursor.execute("SELECT value FROM configs where config_key = 'alarm_running'")
  IS_RUNNING = cursor.fetchone()
  db.commit()
  #print("SHOULD STOP?")
  print(IS_RUNNING[0])
  if IS_RUNNING[0] == 'False':
    print("Stop")
    pixels.brightness = 0
    quit()

try:
  # Sunrise Pattern

  for c in range(math.floor(PIXELS/PIXEL_BAND)):
    shouldStop()
    # Colour
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    for p in range(PIXEL_BAND):
      pixels[(p+PIXELS_COUNTED)] = (r,g,b)

    PIXELS_COUNTED = PIXELS_COUNTED + PIXEL_BAND


  for b in range(RANGE):
    shouldStop()
    BRIGHTNESS = (BRIGHTNESS + BRIGHTNESS_STEP)
    pixels.brightness = BRIGHTNESS

    time.sleep(BRIGHTNESS_DELAY)


  for b in range(RANGE):
    shouldStop()
    pixels.brightness = 0
    time.sleep(0.1)
    pixels.brightness = BRIGHTNESS
    time.sleep(0.1)
  


  while True:
    shouldStop()
    pixels.brightness = 0
    time.sleep(0.05)
    pixels.brightness = BRIGHTNESS
    time.sleep(0.05)
    #config.read("config.txt")

except KeyboardInterrupt:
    print('Keyboard Interrupt')
    pixels.brightness = 0
