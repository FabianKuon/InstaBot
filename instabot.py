from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

class InstagramBot(object):

    def __init__(self, usr, pw):
        self.usr = usr
        self.pw = pw

        #Create a new instance of safari and open instagram
        self.browser = webdriver.Safari()
        self.browser.get('https://instagram.com')
        self.browser.implicitly_wait(5)
        self.insta_login()
        self.destroy_session()

    #Logging into instagram
    def insta_login(self):
        self.browser.find_element_by_name('username').send_keys(self.usr)
        self.browser.find_element_by_name('password').send_keys(self.pw)
        self.browser.find_element_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

    def destroy_session(self):
        self.browser.quit()

if __name__ == "__main__":
    usr = input("Enter instagram username: \n")
    print("Enter your password \n")
    pw = getpass.getpass()
    bot = InstagramBot(usr, pw)

