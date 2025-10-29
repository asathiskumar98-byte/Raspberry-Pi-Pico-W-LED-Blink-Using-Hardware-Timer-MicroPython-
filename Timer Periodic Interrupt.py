import machine
from machine import Timer

# Configure an GPIO as Output LED
led = machine.Pin(16,machine.Pin.OUT)

def timer_callback(timer):
    led.toggle()

tim = Timer(period=1000, mode=machine.Timer.PERIODIC, callback=timer_callback)