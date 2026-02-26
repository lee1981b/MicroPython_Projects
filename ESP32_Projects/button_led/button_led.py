#!/opt/bin/lv_micropython

from machine import Pin

led = Pin(2, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP)

try:
    while True:
        if not button.value():
            led.value(0)
        else:
            led.value(1)
except KeyboardInterrupt:
        led.value(0)