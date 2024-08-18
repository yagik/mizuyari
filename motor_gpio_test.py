import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN1 = 14
PIN2 = 15

GPIO.setup(PIN1,GPIO.OUT)
GPIO.setup(PIN2,GPIO.OUT)


print("Valve Open")
GPIO.output(PIN1, True)
GPIO.output(PIN2, False)
time.sleep(10)

print("Valve Close")
GPIO.output(PIN1, False)
GPIO.output(PIN2, True)
time.sleep(1)

print("GPIO off")
GPIO.output(PIN1,False)
GPIO.output(PIN2,False)
GPIO.cleanup()






GPIO.setwarnings(False)