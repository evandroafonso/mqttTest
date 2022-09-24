import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.SETUP(17, GPIO.OUT)

def temperatura():
    return random.randrange(2, 32)

def umidade():
    return random.randrange(10, 95)

def aquecedor(estado: str):
    if estado == 'on':
        print('Aquecedor LIGADO')
        GPIO.output(17, 1)
    else:
        print('Aquecedor DESLIGADO')
        GPIO.output(17, 0)
