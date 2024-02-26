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
        print("logger initiated")

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



       




class Test_triangle:
    @classmethod
    def setup_class(cls):
        cls.vt = Verify()
        cls.vt.logger.inf("setting up...")

    @classmethod
    def teardown_class(cls):
        cls.vt.logger.info("tearing down...")
        del cls.vt.logger
        del cls.vt


    def test_1(self):
        print("test1")
        self.vt.equilateral()
        assert True == self.vt.check_trinagle()
    def test_2(self):
        print("test2")
        self.vt.driver.refresh()
        self.vt.isoceles()
        assert True == self.vt.check_trinagle()
    def test_3(self):
        print("test3")
        self.vt.driver.refresh()
        self.vt.scalene()
        assert True == self.vt.check_trinagle()
    def test_4(self):
        print("test4")
        self.vt.driver.refresh()
        self.vt.notriangle()
        assert True == self.vt.check_trinagle()


