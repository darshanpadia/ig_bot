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
        if follow_button.text == 'Follow':
            follow_button.click()

    def nav_post_urls_by_tags(self,hashtag,scrolls):
        self.driver.get(f"https://www.instagram.com/explore/tags/{ hashtag }/")
        post_urls = self.find_post_urls(scrolls)
        return post_urls

    def nav_post_urls_by_user_profile(self,profile_name,scrolls):
        self.driver.get(f"https://www.instagram.com/{ profile_name }/")
        post_urls = self.find_post_urls(scrolls)
        return post_urls
        
    def scroll_pages(self,scrolls):
        for i in range(0, scrolls):
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)



    def find_post_urls(self,scrolls):
        post_urls = []
        self.scroll_pages(scrolls)
        posts = self.driver.find_elements_by_tag_name('a')
        for post in posts:
            post_url = post.get_attribute('href')
            if len(post_url) > 26:
                if post_url[26] == 'p':
                    post_urls.append(post_url)
        return post_urls



    def like_post(self,url):  
        self.driver.get(url)
        like_x_path = '//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span'
        like_button = self.driver.find_element_by_xpath(like_x_path)
        current = like_button.get_attribute("aria-label")
        if current == 'Like':
            like_button.click()
        
    def like_posts_in_bunch(self,post_urls):
        for url in post_urls:
            ig_bot.like_post(url)


    
        
            




if __name__ == '__main__':
    ig_bot = InstagramBot('codezytech', 'codezy@tech')
    time.sleep(3)
    developer_posts_urls = ig_bot.nav_post_urls_by_tags('developer',0)
    ig_bot.like_posts_in_bunch(developer_posts_urls)
    camestry_k_profile = ig_bot.nav_post_urls_by_user_profile('camestry_k',0)
    ig_bot.like_posts_in_bunch(camestry_k_profile)
    
