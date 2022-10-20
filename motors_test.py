import os
import time

if os.getenv('MACHINE_CTRL_MOCK_MODE') == '1':
    from mock_gpio import MockGpio
    gpio = MockGpio()
else:
    import RPi.GPIO as gpio

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(27, gpio.OUT)

def forward():
    gpio.output(17, True)
    gpio.output(22, False)
    time.sleep(2)

setup()
pwm = gpio.PWM(27, 500)
pwm.start(45)
forward()
gpio.cleanup()

