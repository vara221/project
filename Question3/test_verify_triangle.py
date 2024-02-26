#from verify_triangle import Verify

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
        self.vt.equilateral()
        assert True == self.vt.check_trinagle()
    def test_2(self):
        self.vt.driver.refresh()
        self.vt.isoceles()
        assert True == self.vt.check_trinagle()
    def test_3(self):
        self.vt.driver.refresh()
        self.vt.scalene()
        assert True == self.vt.check_trinagle()
    def test_4(self):
        self.vt.driver.refresh()
        self.vt.notriangle()
        assert True == self.vt.check_trinagle()


