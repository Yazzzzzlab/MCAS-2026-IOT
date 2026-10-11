import RPi.GPIO as GPIO
import time

PIN = 17  # BCM GPIO17 = 實體腳位 11，請依你的接線調整
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)
        GPIO.output(PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

