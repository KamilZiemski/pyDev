'''
Created on 08 Sep 2015

@author: Kamil
'''

from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo.magentocommerce.com/")

    def test_compare_products_removal_alert(self):
        # get the search textbox
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys("phones")
        search_field.submit()

        # click the Add to compare link
        self.driver.\
            find_element_by_link_text("Add to Compare").click()
            
        # click on Remove this item link, this will display # an alert to the user
        self.driver.find_element_by_link_text("Clear All").click()

        # switch to the alert
        #alert = self.driver.switch_to_alert()
        alert = WebDriverWait(self.driver,10).until(expected_conditions.alert_is_present())

        # get the text from alert
        alert_text = alert.text

        # check alert text
        self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)

        # click on Ok button
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()