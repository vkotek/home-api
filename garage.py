import RPi.GPIO as GPIO
import time

RELAY_PIN = 17  # GPIO pin connected to the optocoupler

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW)

def press_remote():
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RELAY_PIN, GPIO.LOW)
