'''
Created on 07-Mar-2018
@see: Oh God, this guy is freak!
@author: chaitanya
'''

import time
from selenium import webdriver
import autoit

b=webdriver.Chrome(r'C:\Users\chait\Downloads\chromedriver.exe')
b.get(r'https://mbasic.facebook.com/')
raw=input('Enter Something to continue: ')
list1=[r'C:\Users\chait\Desktop\1.jpg', r'C:\Users\chait\Desktop\2.jpg', r'C:\Users\chait\Desktop\3.jpg', r'C:\Users\chait\Desktop\4.jpg',
       r'C:\Users\chait\Desktop\5.jpg', r'C:\Users\chait\Desktop\6.jpg', r'C:\Users\chait\Desktop\7.jpg', r'C:\Users\chait\Desktop\8.jpg',
       r'C:\Users\chait\Desktop\9.jpg', r'C:\Users\chait\Desktop\10.jpg', r'C:\Users\chait\Desktop\11.jpg', r'C:\Users\chait\Desktop\12.jpg',
       r'C:\Users\chait\Desktop\13.jpg', r'C:\Users\chait\Desktop\14.jpg', r'C:\Users\chait\Desktop\15.jpg', r'C:\Users\chait\Desktop\16.jpg',
       r'C:\Users\chait\Desktop\17.jpg', r'C:\Users\chait\Desktop\18.jpg', r'C:\Users\chait\Desktop\19.jpg', r'C:\Users\chait\Desktop\20.jpg',
       r'C:\Users\chait\Desktop\21.jpg', r'C:\Users\chait\Desktop\22.jpg', r'C:\Users\chait\Desktop\23.jpg', r'C:\Users\chait\Desktop\24.jpg']
for i in range(len(list1)):
    b.get(r'https://mbasic.facebook.com/freefolk27')
    time.sleep(2)
    b.find_element_by_xpath(r'//*[@id="timelineBody"]/div[1]/div[1]/form/div[2]/span/div[1]/table/tbody/tr/td[2]/input').click()
    ub=b.find_element_by_xpath(r'//*[@id="root"]/table/tbody/tr/td/form/div[1]/div/input').click()
    time.sleep(3)
    try:
        autoit.win_active(r'Open') 
        autoit.control_send('Open',"Edit1",list1[i])
        autoit.control_send("Open","Edit1","{ENTER}")
    except Exception:
        print('Faultpoint 1')
    time.sleep(5)
    b.find_element_by_xpath(r'//*[@id="root"]/table/tbody/tr/td/form/div[3]/input[1]').click()
    time.sleep(3)
    b.find_element_by_xpath(r'//*[@id="composer_form"]/input[19]').click()
    try:
        b.find_element_by_xpath(r'//*[@id="root"]/table/tbody/tr/td/form/div[5]/input').click()
    except Exception:
        print('Faultpoint 2')
    try:
        b.find_element_by_xpath(r'//*[@id="root"]/table/tbody/tr/td/div[2]/div[1]/a').click()
    except Exception:
        print('Faultpoint 3')
    time.sleep(60)
raw=input('Enter Something to continue: ')
print('U lazy moron!')
b.close()