'''
Created on 30 cze 2015

@author: Kamil
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from __builtin__ import classmethod

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        # create a new Firefox session """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application login page """
        self.driver.get("https://eu1.badoo.com/en/signin/?f=top")

    def test_search_field(self):
        driver = self.driver
        
        #driver.find_element_by_id("email").clean()
        driver.find_element_by_id("email").send_keys("televisor@tlen.pl")
        #driver.find_element_by_id("password").clean()
        driver.find_element_by_id("password").send_keys("Stefan4")
        driver.find_element_by_xpath("//button[@class='btn btn--lg btn--green']").submit()
        driver.find_by_partial_link_text("contains(text(),'%s')]" % ('Chybi')).click()
        #[System.Windows.Forms.SendKeys]::SendWait("{1}")
        #driver.find_element_by_xpath("//a[@class='b-link js-profile-header-vote']").click() 
        
    @classmethod
    def tearDownClass(self):
        # close the browser window
        #self.driver.quit()
        print("konic")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    