# import csv
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import mysql.connector
from selenium.webdriver.support.ui import Select
import time

class tradeMap():
    def __init__(self):
        self.path = r'C:\Users\Tokek Kuning\Documents\data_cakra_kalbe\chromedriver_win32\chromedriver'
        self.driver = webdriver.Chrome(self.path)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized")
        self.driver.get("https://www.trademap.org/Product_SelProduct_TS.aspx?nvpm=1%7c%7c%7c%7c%7cTOTAL%7c%7c%7c2%7c1%7c1%7c2%7c2%7c1%7c1%7c1%7c1%7c1")
        self.wait = WebDriverWait(self.driver, 10)
        time.sleep(10)
    
    def loopingCountryPartner(self):
        dropdowncountry = Select(self.driver.find_element_by_id("ctl00_NavigationControl_DropDownList_Country"))
        dropdowncountry.select_by_index(3)
        # self.count=1
        dropdownpartner= Select(self.driver.find_element_by_id("ctl00_NavigationControl_DropDownList_Partner"))
        # dropdownpartner.select_by_index(3)
        options = dropdownpartner.options
        print(options)
        for index in range(0, len(options) - 1):
            while True:
                try:
                    dropdownpartner= Select(self.driver.find_element_by_id("ctl00_NavigationControl_DropDownList_Partner"))
                    dropdownpartner.select_by_index(index)
                    break
                except:
                    self.driver.refresh()

x = tradeMap()
x.loopingCountryPartner()