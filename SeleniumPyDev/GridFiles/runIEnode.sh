cd "D:\Dev\selenium"
java -Dwebdriver.ie.driver="D:\Dev\selenium\IEDriverServer.exe" -jar selenium-server-standalone-2.47.1.jar -role webdriver -browser "browserName=internet explorer,version=10,maxinstance=1,platform=WINDOWS" -hubHost 192.168.0.12 -port 5555