import RPi.GPIO as GPIO
import time

RELAY_PIN_GARAGE = 27  # GPIO pin connected to the garage
RELAY_PIN_GATE = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN_GARAGE, GPIO.OUT)
GPIO.output(RELAY_PIN_GARAGE, GPIO.LOW)

GPIO.setup(RELAY_PIN_GATE, GPIO.OUT)
GPIO.output(RELAY_PIN_GATE, GPIO.LOW)


def press_remote_garage():
    GPIO.output(RELAY_PIN_GARAGE, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(RELAY_PIN_GARAGE, GPIO.LOW)

def press_remote_gate():
    GPIO.output(RELAY_PIN_GATE, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(RELAY_PIN_GATE, GPIO.LOW)
