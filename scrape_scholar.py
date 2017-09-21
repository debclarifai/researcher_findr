from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver

if __name__ == "__main__":
    driver = init_driver()
