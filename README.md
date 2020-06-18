# ESP8266_Stuff

Good pinout diagrams:  
https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/  

https://docs.micropython.org/en/latest/esp8266/quickref.html#  

https://github.com/dattasaurabh82/micropython-ssd1327/blob/master/ssd1327.py  
```
>>> from machine import I2C, Pin                                                                                      
>>> import ssd1327                                                                                                    
>>> i2c = I2C(scl=Pin(5), sda=Pin(4))                                                                                 
>>> oled = ssd1327.S                                                                                                  
SET_CONTRAST    SET_DISP        SET_COL_ADDR                                                                          
SET_DISP_START_LINE             SET_SEG_REMAP   SET_MUX_RATIO                                                         
SET_DISP_OFFSET                 SET_DISP_CLK_DIV                                                                      
SET_PRECHARGE   SET_VCOM_DESEL  SET_SCROLL_DEACTIVATE                                                                 
SET_ROW_ADDR    SET_DISP_MODE   SET_FN_SELECT_A                                                                       
SET_PHASE_LEN   SET_SECOND_PRECHARGE                                                                                  
SET_GRAYSCALE_TABLE             SET_GRAYSCALE_LINEAR                                                                  
SET_FN_SELECT_B                 SET_COMMAND_LOCK                                                                      
SSD1327         SSD1327_I2C     SEEED_OLED_96X96                                                                      
>>> oled = ssd1327.SSD1327_I2C(128,128,i2c,addr=60)                                                                   
>>> oled.fill(1)                                                                                                      
>>> oled.show()                                                                                                       
>>> oled.fill(0)                                                                                                      
>>> oled.show()                                                                                                                                                                                       
>>> oled.text("Hello",0,0)                                                                                            
>>> oled.show()                                                                                                       
>>>                                                                                                                   
```

