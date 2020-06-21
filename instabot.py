from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

class InstagramBot:

    def __init__(self, usr, pw):
        """
        Initializes an inistance of the InstagramBot class

        Args:
            usr:str: The Instagram username for a user
            pw:str: The Instagram password for a user

        """

        self.usr = usr
        self.pw = pw
        self.main_url = 'https://www.instagram.com'

        #Open either Safari or internet explorer
        try:
            self.browser = webdriver.Safari()
        except:
            self.browser = webdriver.Ie()

        #Open instagram login page
        self.browser.get('https://instagram.com/accounts/login/')

        #Wait until web page is fully loaded
        self.browser.implicitly_wait(5)

        #Logging into instagram
        self.insta_login()

        #Follow other instagram users
        self.subscribe_to_user()

        #destroy session at the end
        self.destroy_session()

    #Logging into instagram
    def insta_login(self):
        self.browser.find_element_by_name('username').send_keys(self.usr)
        self.browser.find_element_by_name('password').send_keys(self.pw)
        self.browser.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

    #Open a instagram page by username
    def user_page(self, username):
        self.browser.get('{}/{}'.format(self.main_url, username))

    #Subscribe to a user instagram account
    def subscribe_to_user(self, user):
        self.user_page(user)
        self.browser.find_element_by_name('follow').click()

    def destroy_session(self):
        self.browser.quit()

def read_txt_file(path):
    result = []
    with open(path) as file:
        for line in file:
            result.append(line.strip())
    return result

if __name__ == "__main__":
    usr, pw = read_txt_file('UserProfile.txt')
    bot = InstagramBot(usr, pw)

