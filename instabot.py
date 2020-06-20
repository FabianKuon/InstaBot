from time import sleep
from selenium import webdriver
import getpass

class InstagramBot(object):

    def __init__(self, driver_settings, usr, pw):
        self.usr = usr
        self.pw = pw
        self.driver_settings = driver_settings
        self.driver_path, self.brave_path = self.Txt_File_to_String(driver_settings)

        #Create object of ChromeOptions class
        option = webdriver.ChromeOptions()
        option.binary_location = self.driver_path

        #Create a new instance of chrome
        browser = webdriver.Chrome(executable_path = self.brave_path ,
                                   chrome_options = option)

        #Set the path of the brave browser
        options.setBinary("Applications/Brave Browser.app")
        self.browser.get('https://www.instagram.com')
        self.browser.find_element_by_xpath("").send_keys(usr)
        self.browser.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)

        self.browser.find_element_by_xpath('//button[@type="submit"]').click

        self.slep(4)
        self.browser.quit()


    def Txt_File_to_String(self, driver_settings):
        data = []
        with open(driver_settings) as f:
            for line in f:
                data.append(line.strip())
        return data


def main():
    usr = input("Enter instagram username: \n")
    print("Enter your password \n")
    pw = getpass.getpass()
    bot = InstagramBot('DriverSettings.txt', usr, pw)
    bot.Txt_File_to_String()

if __name__ == "__main__":
    main()
