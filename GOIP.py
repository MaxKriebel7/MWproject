import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.LOW)
GPIO.output(8, GPIO.HIGH)

for i in range(10):
    GPIO.output(8, GPIO.LOW)
    time.sleep(1)
    GPIO.output(8, GPIO.HIGH)
    time.sleep(1)
