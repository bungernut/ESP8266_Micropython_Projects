# main.py script for ESP8266
gc.collect()
print('[main]')
print('Welcome to the ESP8266 Huzzah!')
 
if not wlan.isconnected():
    print('Wifi not connected')
else:
    print('ip :', ip)
    print('netmask:', netmask)
    print('gateway:', gateway)
    print('DNS :', dns)
    print('MAC :', ubinascii.hexlify(wlan.config('mac'),':').decode('utf-8'))

import webrepl
#webrepl.start()

print("Starting up button pusher")
#import uasyncio
from machine import I2C, Pin, RTC
import ntptime
import utime
import time
# start real time clock
rtc = RTC()
# Set the RTC with NTP
ntptime.settime()
localtime_offset = 7*3600

button = Pin(2, Pin.IN, pull=Pin.PULL_UP)

import ssd1327
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = ssd1327.SSD1327_I2C(128,128,i2c,addr=60)

def get_currtime():
    y,m,d,H,M,*_ = utime.localtime(utime.time()-localtime_offset)
    return "%d/%d %d:%d"%(m,d,H,M)

def display(ft):
    ctime = "* " + get_currtime() + " *"
    col = int((128-(len(ctime)*8))/2.0)
    oled.fill(0)
    oled.text(ctime, col, 1)
    for i in range(min(len(ft), 8)):
        oled.text("%d) %s"%(-i-1,ft[-i-1]), 0, 12*(i+2))
    oled.show()

def display_off():
    oled.fill(0)
    oled.show()

pressed_i = 0
pressed_loops = 0
last_press = 0.0
feed_times = []
sleeping = True
while True:
    if sleeping == False:
        if button.value() == 1:
            # Button is not pressed
            if pressed_i > 0:
                pressed_loops = pressed_i
                pressed_i = 0
        elif button.value() == 0:
            # Button is pressed
            last_press = utime.time()
            pressed_loops = 0
            pressed_i += 1
        
        if pressed_loops > 0  and pressed_loops < 8:
            print("short press")
            pressed_loops = 0
            feed_times.append(get_currtime())
            display(feed_times)
        elif pressed_loops >= 8:
            print("long press", pressed_loops)
            pressed_loops = 0
            feed_times.pop(-1)
            display(feed_times)

    if sleeping == True and button.value() == 0:
        sleeping = False
        last_press = utime.time()
        display(feed_times)

    if utime.time() - last_press > 60:
        display_off()

    if len(feed_times) > 20:
        # Delete old feed times
        feed_times.pop(0)
        
    time.sleep(0.05)
