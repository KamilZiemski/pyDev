'''
Created on 30 cze 2015

@author: Kamil
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):

    def setUp(self):
        
        
        desired_caps = {}
        desired_caps['platform'] = 'MAC'
        desired_caps['browserName'] = 'firefox'

        self.dirver = \
            webdriver.Remote('http://192.168.0.3:4444/wd/hub',desired_caps)
        # navigate to the application home page """
        self.driver.get("http://demo.magentocommerce.com/")
        # create a new Firefox session """
        # cls.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        
        
    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.NAME,"q"))

    def test_language_option(self):
        # check language options dropdown on Home page
        self.assertTrue(self.is_element_present(By.ID,"select-language"))

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = \
            self.driver.find_element_by_css_selector("div.header-minicart span.icon")
        shopping_cart_icon.click()
        
        #comment
        shopping_cart_status = \
            self.driver.find_element_by_css_selector("p.empty").text
        self.assertEqual("You have no items in your shopping cart.", shopping_cart_status)

        close_button =  self.driver.find_element_by_css_selector("div.minicart-wrapper a.close")
        close_button.click()

    
    def tearDown(self):
        # close the browser window
        self.driver.quit()

        
        
if __name__ == '__main__':
    unittest.main()