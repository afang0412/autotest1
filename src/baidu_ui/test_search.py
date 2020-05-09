import pytest
import xlrd
from selenium import webdriver
from time import sleep,ctime
import os
from .const import *


class Test_baidu_search():
    def test_search_from_excel(self,excel_dir=EXCEL_DIR):

        driver=webdriver.Chrome()
        driver.get("http://www.baidu.com")
        #打开excel
        excel_file=xlrd.open_workbook(EXCEL_DIR)
        #获取第一个sheet
        sheet=excel_file.sheet_by_index(0)
        #获取第一列数据，返回列表
        cols=sheet.col_values(0)
        print(cols)
        #遍历列表，拿取数据作为测试输入
        for query in cols:
            #每次循环换关键词时文本框会清空
            driver.find_element_by_id("kw").clear()
            #send_keys只接受str格式
            driver.find_element_by_id("kw").send_keys(str(query))
            #单击响应
            driver.find_element_by_id("su").click()
            sleep(2)
    def test_ssss(self):
        #todo..........
        print("11111111111111111111111111111111")
        #断言
        assert 1==1
    #def teat_failed(self):
        #print("22222222222222222222222222222222")
       # assert 1==0