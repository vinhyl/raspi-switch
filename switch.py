#coding: utf8
import sys
import RPi.GPIO as GPIO
import time

PORT = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PORT, GPIO.OUT)


def high():
    GPIO.output(PORT, GPIO.HIGH)


def low():
    GPIO.output(PORT, GPIO.LOW)


def open():
    low()
    time.sleep(2)
    high()
    GPIO.cleanup()


if sys.argv[1] == "open":
    low()
    time.sleep(2)
    high()
    GPIO.cleanup()
elif sys.argv[1] == "close":
    GPIO.cleanup()
