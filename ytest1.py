# coding = utf-8
from selenium import webdriver
from time import sleep, ctime
import os

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("Test search")
driver.find_element_by_id("su").click()
sleep(10)
driver.quit()