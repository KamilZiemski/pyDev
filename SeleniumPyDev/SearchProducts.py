'''
Created on 29 wrz 2015

@author: Kamil
'''
import sys
import unittest
from selenium import webdriver

class SearchProducts(unittest.TestCase):

    PLATFORM = 'WINDOWS'
    BROWSER = 'phantomjs'
    SAUCE_USERNAME = 'markopolo'
    SUACE_KEY = '1e4b7395-9449-44c1-a498-abecca1bd1ed'

    def setUp(self):

        desired_caps = {}
        desired_caps['platform'] = self.PLATFORM
        desired_caps['browserName'] = self.BROWSER
        
        #sauce_string = self.SAUCE_USERNAME + ':' + self.SUACE_KEY

        #self.driver = \
        #    webdriver.Remote('http://' + sauce_string + '@ondemand.saucelabs.com:80/wd/hub', desired_caps)
            
        self.driver = \
            webdriver.Remote('http://192.168.0.3:4444/wd/hub',desired_caps)
        #self.driver = webdriver.Firefox()
        self.driver.get('http://demo.magentocommerce.com/')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def testSearchByCategory(self):

        # get the search textbox
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys('phones')
        self.search_field.submit()

        # get all the anchor elements which have product names # displayed currently on result page using # find_elements_by_xpath method
        products = self.driver.\
            find_elements_by_xpath('//h2[@class=\'product-name\']/a')

        # check count of products shown in results
        self.assertEqual(3, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        SearchProducts.BROWSER = sys.argv.pop()
        SearchProducts.PLATFORM = sys.argv.pop()
    unittest.main(verbosity=2)