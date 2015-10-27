#!/usr/bin/env bash
java -Dwebdriver.ie.driver=d:/Dev/Selenium/IEDriverServer.exe" -Dwebdriver.chrome.driver=d:/Dev/Selenium/chromedriver.exe" -jar d:/Dev/selenium/selenium-server-standalone-2.47.1.jar

java -Dwebdriver.ie.driver="C:\SeDrivers\IEDriverServer.exe" -jar selenium-server-standalone-2.41.0.jar -role webdriver -browser "browserName=internet explorer,version=10,maxinstance=1,platform=WINDOWS" -hubHost 192.168.1.103 –port 5555