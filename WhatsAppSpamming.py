'''
Created on 13-Jul-2016
@see: Web Scraping
@author: Chaitanya027
'''

import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
b = webdriver.Firefox(firefox_binary=binary)
b.get('https://web.whatsapp.com')
#Enter Something on Console after connecting to WhatsApp Web
input()
elem = b.find_element_by_xpath('//span[contains(text(),"YOUR_TARGET_NAME_HERE")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
print('Please enter a message you wish to spam ',end='')
message=input()
print('Please specify sleep duration in seconds ',end='')
sec=int(input())
while True:
    elem1[1].send_keys(message)
    b.find_element_by_class_name('send-container').click()
    time.sleep(sec)