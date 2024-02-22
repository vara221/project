import pytest
import logging
from sele_project.webelement import WebTest


class TestGrp:

    # Setup method

    @classmethod
    def setup_class(cls):
        cls.webTst = WebTest()
        cls.webTst.logger = logging.getLogger()
        cls.webTst.logger.info("Setup...starting the tests")

    # Teardown method
    @classmethod
    def teardown_class(cls):
        cls.webTst.logger.info("Tearing down...")
        del cls.webTst.logger
        del cls.webTst


    def test_one(self):
       # self.webTst.clickFirstItem()
        self.webTst.logger.info("Test1")
        result = self.webTst.isFirstItemClicked()
        print(result,"gjhkjktrhgfjuhjuhuyuijyilkuoiluoluluikhjgfyr5r4e")
        assert True == result

    def test_two(self):
        # self.webTst = WebElements.WebTest()
        self.webTst.clickSecondItem()
        self.webTst.logger.info("Test2")
        result = self.webTst.isSecondItemClicked()
        assert True == result