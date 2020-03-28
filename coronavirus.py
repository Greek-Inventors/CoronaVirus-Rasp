#!/usr/bin/python3

import I2C_LCD_driver
import time
from bs4 import BeautifulSoup
import requests
import os
import smtplib
import socket

mylcd = I2C_LCD_driver.lcd()

# Insert your URL here
url_c = "https://corona.help/country/Greece"

infections = "0"

while True:
    try:

        ''' email account and send '''
        def alarmmail():
            try:
                check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                to1 = 'emailtosend@gmail.com'
                gmail_user = 'youremail@gmail.com'
                gmail_pwd = 'yourpassword'
                smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo()
                smtpserver.login(gmail_user, gmail_pwd)
                header = 'To:' + to1 + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: Corona Virus - Covid-19 - ALARM \n'
                msg = header + '\n Corona Virus Results ' + ' Infections: ' + str(infections_c) + ', Deaths: '+ str(deaths_c) + ', Survived: ' + str(survived_c) + '\n\n' + 'This is the Corona Virus Day Report From Raspberry System Virus Update' + '\n\n'
                smtpserver.sendmail(gmail_user, to1, msg.encode("utf-8", errors="ignore"))
                smtpserver.close()
        
            except socket.error as err:
                pass
        
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
    
        if (str(infections_c) > infections):
            infections = str(infections_c)
            os.system('mplayer -really-quiet sound.mp3 &')
            alarmmail()
        
        mylcd.lcd_display_string("Deaths: " + deaths_c, 2)
        time.sleep(5)
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Surviv: " + survived_c ,1)
        mylcd.lcd_display_string("Greece -- Update" ,2)
        time.sleep(5)
        mylcd.lcd_clear()
        
    except:
        mylcd.lcd_clear()
    
    
