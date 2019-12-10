from selenium import webdriver
import os
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com"
        self.driver = webdriver.Chrome('./chromedriver.exe')
        
        self.login()

    def login(self):
        self.driver.get(f'{self.base_url}/accounts/login/')
        time.sleep(3)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

    def nav_user(self,user):
        self.driver.get(f'{self.base_url}/{user}/')

    def follow_user(self,user):
        self.nav_user(user)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/button/').click()
if __name__ == '__main__':
    ig_bot = InstagramBot('codezytech', 'codezy@tech')
    time.sleep(3)
    ig_bot.follow_user('darshanpadia')
    
