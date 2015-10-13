'''
Created on 28 lip 2015

@author: Kamil
'''
import unittest
import HTMLTestRunner
import os
from SeleniumPyDev import HomePageTest
from SeleniumPyDev import SearchTest

# get the directory path to output report file
dir = os.getcwd()
print(dir)

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest.SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest.HomePageTest)

# create a test suite combining search_test and home_page_test
#smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

smoke_tests = unittest.TestSuite([search_tests])

# open the report file
reportFilePath = dir + "\SmokeTestReport.html"
outfile = open(reportFilePath, "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
                 stream=outfile,
                 title='Test Report',
                 description='Smoke Tests'
                 )

# run the suite using HTMLTestRunner
runner.run(smoke_tests)