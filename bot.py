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
        #driver = self.driver()    
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
        follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
        print(follow_button).text()

    def nav_posts_by_tags(self,hashtag):
        post_urls = []
        self.driver.get(f"https://www.instagram.com/explore/tags/{ hashtag }/")
        for i in range(0, 3):
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
        a_tags = self.driver.find_elements_by_tag_name('a')
        for tag in a_tags:
            post_url = tag.get_attribute('href')
            if len(post_url) > 26:
                if post_url[26] == 'p':
                    post_urls.append(post_url)
        return post_urls

    def like_post(self,post_urls):
        for url in post_urls:
            self.driver.get(url)
            like_x_path = '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span'
            like_button = self.driver.find_element_by_xpath(like_x_path)
            like_button.click()
            time.sleep(8)
                    




if __name__ == '__main__':
    ig_bot = InstagramBot('codezytech', 'codezy@tech')
    time.sleep(3)
    developer_posts = ig_bot.nav_posts_by_tags('developer')
    ig_bot.like_post(developer_posts)
    
    
