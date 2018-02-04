# conding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class BrowserHandling:
    '''
    def __init__(self, url, driver_path):
        self._url = url
        self._driver_path = driver_path

    # open url path
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def driver_path(self):
        return self._driver_path

    @driver_path.setter
    def driver_path(self, driver_path):
        self._driver_path = driver_path
    '''

    @classmethod
    def control_browser(self, url, driver_path):
        # Maximize Browser option
        options = webdriver.ChromeOptions()
        options.add_argument("--kiosk")

        driver = webdriver.Chrome(executable_path = driver_path,
                                  chrome_options = options)
        #driver = webdriver.Chrome(chrome_options=options)

        driver.get(url)
        '''
        driver.find_element_by_id("lst-ib").send_keys("selenium")
        driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)

        driver.find_element_by_link_text("Selenium - Web Browser Automation")
        '''

        #driver.find_element_by_class_name('btn btn-github-inverse btn-block landingOauthSignup_button').send_keys(Keys.ENTER)
        #driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[3]').send_keys(Keys.ENTER)

        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/a[1]').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="login_field"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[3]').send_keys(Keys.ENTER)

        driver.find_element_by_css_selector('div.st-Header_community').send_keys(Keys.ENTER)

        sleep(5)
        driver.find_element_by_xpath('//*[@id="appRoot"]/div/div[1]/div/div[1]/div[3]/div[2]/a[1]').send_keys(Keys.ENTER)

        sleep(5)
        driver.close()
