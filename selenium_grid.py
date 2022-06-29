import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




def test_grid():
    driver = webdriver.Remote(command_executor='http://192.168.174.128:5001/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
    driver.get('https://www.baidu.com')
    print("运行成功啦～～～")


def test_grid2():
    driver = webdriver.Remote(command_executor='http://192.168.174.128:5001/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
    driver.get('https://www.baidu.com')
    print("运行成功啦～～～")