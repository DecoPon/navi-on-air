# conding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class BrowserHandling:

    @classmethod
    def browser_control(self):
        # Maximize Browser option
        options = webdriver.ChromeOptions()
        options.add_argument("--kiosk")

        # driver = webdriver.Chrome(executable_path="driver/chromedriver")
        driver = webdriver.Chrome(chrome_options=options)

        driver.get("https://www.google.co.jp/")

        driver.find_element_by_id("lst-ib").send_keys("selenium")
        driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)

        driver.find_element_by_link_text("Selenium - Web Browser Automation")

        sleep(5)

        driver.close()
