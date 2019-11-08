'''
Created on 14-Jul-2016
@see: To get poornima attendance directly.
@author: Chaitanya027
'''


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys,re
from _ast import Try
sys.argv
if len(sys.argv)>0:
    #b=webdriver.PhantomJS(r'C:\Users\Chaitanya027\AppData\Local\Programs\Python\Python35-32\Lib\phantomjs\bin\phantomjs.exe')
    b=webdriver.Chrome(r'C:\Users\Chaitanya027\AppData\Local\Programs\Python\Python35-32\Scripts\chromedriver.exe')
    #binary=FirefoxBinary('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk')
    #b=webdriver.Firefox()
    b.get('http://www.poornima.org/attendance/')
    for i in sys.argv[1:]:
        try:
            clgRegex=re.compile(r'(\w\w\w?\w)/(\w\w)/(\d\d)/(\d\d\d)')
            clg=clgRegex.search(i)
            elem=b.find_element_by_css_selector('#content > div > div > div > form > div:nth-child(1) > select')
            elem.send_keys((clg.group(1).upper()))
            elem= b.find_element_by_css_selector('#content > div > div > div > form > div:nth-child(2) > p > select')
            if clg.group(3)== str(13):
                elem.send_keys('IVth Year')
            elif clg.group(3)==str(14):
                elem.send_keys('IIIrd Year')
            elif clg.group(3)==str(15):
                elem.send_keys('IInd Year')
            elif clg.group(3)==str(16):
                elem.send_keys('Ist Year')
            elem=b.find_element_by_css_selector('#content > div > div > div > form > div:nth-child(3) > p:nth-child(2) > input[type="text"]')
            elem.clear()
            elem.send_keys(i)
            b.find_element_by_class_name('button').click()
            elem=b.find_element_by_css_selector('#content > div > div > div > div.col-md-12 > table > tbody > tr:nth-child(2) > td:nth-child(6)')
            elem2=b.find_element_by_css_selector('#content > div > div > div > div.col-md-12 > table > tbody > tr:nth-child(2) > td:nth-child(3)')
            print(elem2.text+ ', your attendence is '+elem.text+'%')
        except Exception:
            print('NO STUDENT EXISTS')
    b.quit()
else:
    sys.exit()
    
