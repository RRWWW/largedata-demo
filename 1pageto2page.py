# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 1pageto2page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.agoda.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1pageto2page(self):
        driver = self.driver
        driver.get(self.base_url + "/zh-tw/pages/agoda/default/DestinationSearchResult.aspx?asq=zWuVSTFwAmUZtJhrjzSYyyJ%2b8Pr%2bb3vIcWHNz0nChxYiiT8zNDXLvw%2fWMmWL8C%2fa7f90OGPtD9oCQ4NudA5BZzB04uu8mJ8oLI3FEDc5TFW4FYxikhYAHeur9242UHyVn327yZdwPfRzYZTCDrJYgX2Cypg9MGrroCOhd5x1%2bJR6pLhPh9qkXdjgD40yG3KJxJI8JYnZ1kv5yHlu1CSWFHZIhBFd8YZ62P9YcGAeOSbd4F9I2vdLJQBbcvu%2fn56yaIvsrMsvtuYWUIv%2bP1MgDlur%2ftc%2b54Iv4fnCDM4f8d8%3d&cid=1732641&tag=a1570cea-9c19-49db-a5e7-3e25a3f8920d&tick=635916595246&sort=agodaRecommended")
        driver.find_element_by_id("paginationNext").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
