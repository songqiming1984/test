from selenium import webdriver
import time
import sys


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(3)
print(sys.argv[0])
driver.close()