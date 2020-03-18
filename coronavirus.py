#!/usr/bin/python3

import I2C_LCD_driver
import time
from bs4 import BeautifulSoup
import requests
import os

mylcd = I2C_LCD_driver.lcd()

# Insert your URL here
url_c = "https://corona.help/country/Greece"

infections = 0

while True:
    try:
        # Print to LCD
        mylcd.lcd_display_string("Time: %s" %time.strftime("  %H:%M"), 1)
        mylcd.lcd_display_string("Date: %s" %time.strftime("%d/%m/%Y"), 2)
        time.sleep(2)

        try:
            # Read CoronaVirus
            page_c = requests.get(url_c)
            soup_c = BeautifulSoup(page_c.text, 'html.parser')
    
            # print (soup)
            infections_c = soup_c.select('h2')[1].text.strip()
            deaths_c = soup_c.select('h2')[2].text.strip()
            survived_c = soup_c.select('h2')[3].text.strip()
        except:
            mylcd.lcd_clear()

        mylcd.lcd_clear()

        # Print LCD
        mylcd.lcd_display_string("Infect: " + infections_c, 1)
    
        if (int(infections_c) > infections):
            infections = int(infections_c)
            os.system('mplayer -really-quiet sound.mp3 &')
        
        mylcd.lcd_display_string("Deaths: " + deaths_c, 2)
        time.sleep(5)
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Surviv: " + survived_c ,1)
        mylcd.lcd_display_string("Greece -- Update" ,2)
        time.sleep(5)
        mylcd.lcd_clear()
    except:
        mylcd.lcd_clear()
    
    
