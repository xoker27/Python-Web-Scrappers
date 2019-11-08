'''
Created on 17-Jan-2017
@see: To track online activity of a user.
@author: chait
'''

import time
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
b = webdriver.Firefox(firefox_binary=binary)
b.get('https://web.whatsapp.com')
input()
elem = b.find_element_by_xpath('//span[contains(text(),"Chaitanya")]')
elem.click()
elem1 = b.find_elements_by_css_selector('div.chat-status:nth-child(2) > span:nth-child(1)')
print(elem1)
'''while True:
    elem1[1].send_keys(message)
    b.find_element_by_class_name('send-container').click()
    time.sleep(sec)
    now = datetime.datetime.now()
    print(now)'''