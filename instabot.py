from time import sleep
from selenium import webdriver
import getpass

class InstagramBot(object):

    def __init__(self, usr, pw):
        self.usr = usr
        self.pw = pw

        self.browser = webdriver.Safari()
        self.browser.get('https://www.instagram.com')
        self.browser.find_element_by_xpath("//input[@name=\"username\"]").send_keys(usr)
        self.browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)

        self.browser.find_element_by_xpath('//button[@type="submit"]').click

        self.slep(4)
        self.browser.quit()


def main():
    usr = input("Enter instagram username: \n")
    print("Enter your password \n")
    pw = getpass.getpass()
    bot = InstagramBot(usr,pw)

if __name__ = "__main__":
    main()
