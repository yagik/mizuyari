import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN1 = 14
PIN2 = 15

GPIO.setup(PIN1,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)


print("Valve Open")
GPIO.output(PIN1, True)
GPIO.output(PIN2, False)
