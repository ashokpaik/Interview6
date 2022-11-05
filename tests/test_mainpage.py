import pytest

from testdata.mainpagedata import Mainpagedata
from testpageobjects.mainpageobjects import Mainpageobjects
from utilities.BaseClass import BaseClass


class Testmainpage(BaseClass):

    @pytest.fixture(params=Mainpagedata.getTestData("TestCase1"))
    def getdata(self, request):
        return request.param

    def test_mainpage(self, getdata):
        log = self.getLogger()
        log.info("Name is" + getdata["Firstname"])
        mainpageobjects = Mainpageobjects(self.driver)
        mainpageobjects.name().send_keys(getdata["Firstname"])
        mainpageobjects.email().send_keys(getdata["Email"])
        mainpageobjects.password().send_keys(getdata["Password"])
        mainpageobjects.check().click()
        mainpageobjects.select().send_keys("Female")
        mainpageobjects.radio().click()
        mainpageobjects.bday().send_keys(getdata["Birthday"])
        mainpageobjects.btn().click()
        msg = mainpageobjects.alert().text
        assert "Success" in msg
        self.driver.refresh()
