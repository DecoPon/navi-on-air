import configparser
import requests
import json

from Browser_Handling import BrowserHandling


class Main:

    @classmethod
    def main(self):
        browser = BrowserHandling()
        browser.browser_control()


if __name__ == '__main__':
    Main.main()
