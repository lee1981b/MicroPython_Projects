#!/opt/bin/lv_micropython
from time import sleep_ms
from machine import Pin

def run():
    led = Pin(2, Pin.OUT)
    try:
        while True:
            led.value(1)
            sleep_ms(1000)
            led.value(0)
            sleep_ms(1000)
    except KeyboardInterrupt:
        led.value(0)