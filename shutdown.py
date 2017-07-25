# put this file into the Desktop
import RPi.GPIO as GPIO
import time import os
buttonPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_state = True

input_state = True

while True:
  input_state = GPIO.input(buttonPin)

  if (not input_state):
    print("Shutdown")
    os.system('sudo shutdown -h now')
    time.sleep(0.05)
    GPIO.cleanup()

