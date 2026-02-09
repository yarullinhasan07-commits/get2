import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
deli = 6
GPIO.setup(deli, GPIO.IN)
while True:
    state = GPIO.input(deli)
    if state == 1:
        GPIO.output(led, 0)    
    else: GPIO.output(led, 1)
    time.sleep(0.1)