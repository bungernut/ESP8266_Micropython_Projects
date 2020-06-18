# ESP8266_Stuff

Good pinout diagrams:  
https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/  

https://docs.micropython.org/en/latest/esp8266/quickref.html#  

https://github.com/dattasaurabh82/micropython-ssd1327/blob/master/ssd1327.py  
```
>>> from machine import I2C, Pin                                                                                      
>>> import ssd1327                                                                                                    
>>> i2c = I2C(scl=Pin(5), sda=Pin(4))                                                                                                                                                      
>>> oled = ssd1327.SSD1327_I2C(128,128,i2c,addr=60)                                                                   
>>> oled.fill(1)                                                                                                      
>>> oled.show()                                                                                                       
>>> oled.fill(0)                                                                                                      
>>> oled.show()                                                                                                                                                                                       
>>> oled.text("Hello",0,0)                                                                                            
>>> oled.show()                                                                                                       
>>>                                                                                                                   
```

