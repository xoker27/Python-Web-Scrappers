'''
Created on 07-Feb-2017
@see: To clean up gmail inbox :)
@author: Chaitanya027
'''


import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
b = webdriver.Firefox(firefox_binary=binary)
#b=webdriver.PhantomJS(r'F:\Eclipse_Workspace\phantomjs-2.1.1-windows\bin\phantomjs.exe')
b.get(r'https://www.google.com/gmail/')
email=input().split()
b.find_element_by_css_selector('#Email').send_keys(email[0])
b.find_element_by_css_selector('#next').click()
time.sleep(10)
b.find_element_by_css_selector('#Passwd').send_keys(email[1])
b.find_element_by_css_selector('#signIn').click()
time.sleep(60)
while True:
    b.find_element_by_css_selector(r'span.T-Jo > div:nth-child(1)').click()
    time.sleep(30)
    b.find_element_by_css_selector(r'.nX').click()
    time.sleep(30)
b.quit()