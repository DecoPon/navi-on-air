import configparser
import requests
import json

from Browser_Handling import BrowserHandling


class Main:

    @classmethod
    def main(self):

        # read config
        config = configparser.ConfigParser()
        config.read('config.ini')

        url = config["app_settings"]["url"]
        driver_path = config["app_settings"]["driver_path"]

        browser = BrowserHandling()
        browser.control_browser(url, driver_path)


if __name__ == '__main__':
    Main.main()
