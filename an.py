from selenium import webdriver
import time
import sys


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(3)
print('执行脚本绝对路径：'+sys.argv[0])
print('执行脚本相对路径：'+__file__)
driver.close()