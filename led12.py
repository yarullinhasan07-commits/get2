import RPi.GPIO as GPIO
import time
botton = 13
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(botton, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
state = 0
while True:
    if GPIO.input(botton):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)
        print(state)


