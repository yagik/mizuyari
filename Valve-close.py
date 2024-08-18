import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN1 = 14
PIN2 = 15

GPIO.setup(PIN1,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)

print("Valve Close")
GPIO.output(PIN1, False)
GPIO.output(PIN2, True)
time.sleep(1)

GPIO.output(PIN2, False)
