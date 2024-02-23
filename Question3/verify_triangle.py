from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import logging


class Verify:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testpages.eviltester.com/styled/apps/triangle/triangle001.html")
        self.driver.maximize_window()
        self.logger = logging.getLogger(__name__)
        self.fh = logging.FileHandler("log3.log")
        self.fmt = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s- %(message)s")
        self.fh.setFormatter(self.fmt)
        self.logger.addHandler(self.fh)
        self.logger.setLevel(logging.DEBUG)

    def equilateral(self):
        self.logger.info("checking equilateral triangle")
        self.driver.find_element(By.ID,"side1").send_keys(5)
        self.driver.find_element(By.ID,"side2").send_keys(5)
        self.driver.find_element(By.ID,"side3").send_keys(5)
        self.driver.find_element(By.ID,"identify-triangle-action").click()

    def isoceles(self):
        self.logger.info("checking isoceles triangle")
        self.driver.find_element(By.ID, "side1").send_keys(5)
        self.driver.find_element(By.ID, "side2").send_keys(4)
        self.driver.find_element(By.ID, "side3").send_keys(5)
        self.driver.find_element(By.ID, "identify-triangle-action").click()

    def scalene(self):
        self.logger.info("checking scalene triangle")
        self.driver.find_element(By.ID, "side1").send_keys(5)
        self.driver.find_element(By.ID, "side2").send_keys(6)
        self.driver.find_element(By.ID, "side3").send_keys(7)
        self.driver.find_element(By.ID, "identify-triangle-action").click()

    def notriangle(self):
        self.logger.info("checking no triangle")
        self.driver.find_element(By.ID, "side1").send_keys(5)
        self.driver.find_element(By.ID, "side2").send_keys(1)
        self.driver.find_element(By.ID, "side3").send_keys(4)
        self.driver.find_element(By.ID, "identify-triangle-action").click()

    def check_trinagle(self):
        s = self.driver.find_element(By.ID, "identify-triangle-action")
        if s.is_enabled():
            return True
        else:
            return False


"""" def check_side1(self):
        self.logger.info("checking side1 textbox")
        self.driver.find_element(By.ID,"side1").send_keys(5)
        s1 = self.driver.find_element(By.ID,"side1")
        return s1.get_attribute("value")

    def check_side2(self):
        self.driver.find_element(By.ID,"side2").send_keys(5)
        self.logger.info("checking side2 textbox")
        s2 = self.driver.find_element(By.ID, "side1")
        return s2.get_attribute("value")

    def check_side3(self):
        self.driver.find_element(By.ID,"side3").send_keys(5)
        self.logger.info("checking side3 textbox")
        s3 = self.driver.find_element(By.ID,"side1")
        return s3.get_attribute("value")

    def check_identify_button(self):
        self.driver.find_element(By.ID,"identify-triangle-action").click()
        self.logger.info("checking identify triangle button")
        s = self.driver.find_element(By.ID,"identify-triangle-action")
        if s.is_enabled():
            return True
        else:
            return False
"""





