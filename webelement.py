import logging
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


class WebTest:
    def __init__(self):
        self.chrome_driver = webdriver.Chrome()
        self.chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.chrome_driver.maximize_window()
        self.logger = logging.getLogger(__name__)
        self.fh = logging.FileHandler("log1.log")
        self.fmt = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        self.fh.setFormatter(self.fmt)
        self.logger.addHandler(self.fh)
        self.logger.setLevel(logging.DEBUG)


    def clickFirstItem(self):
        first_element = self.chrome_driver.find_element(By.NAME, "li1")
        f = first_element.is_selected()
        print(f,"before clickedddddddddddddddddddddddddddddd")
        # first_element.click()
        print(f,"after clickedddddddddddddddddddddddddddddd")
        self.logger.info("First item clicked")
        sleep(5)

    def isFirstItemClicked(self):
        first_element = self.chrome_driver.find_element(By.NAME, "li1")
        if first_element.is_selected() :
            return True
        else:
            return False

    def clickSecondItem(self):
        first_element = self.chrome_driver.find_element(By.NAME, "li2")
        first_element.click()
        self.logger.info("Second item clicked")
        sleep(5)

    def isSecondItemClicked(self):
        second_element = self.chrome_driver.find_element(By.NAME, "li2")
        if second_element.is_enabled():
            return True
        else:
            return False