from selenium import webdriver
import time
import Constants



class InstaBot:
    def __init__(self,username,password):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(Constants.instagram_url)
        self.username=username
        self.driver.find_element_by_xpath(Constants.username_xpath).send_keys(username)
        self.driver.find_element_by_xpath(Constants.password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(Constants.login_button_xpath).click()
        try:
            self.driver.find_element_by_xpath(Constants.turn_on_notifications_xpath).click()
        except:
            print("Notifications are already on")


    def get_followers_list(self):
        self.driver.find_element_by_xpath(Constants.followers_xpath.format(self.username)).click()

        scroll_box_followers=self.driver.find_element_by_xpath(Constants.scroll_box_xpath)
        
        scroll_start=0
        scroll_end=1

        while True:
            if scroll_start!=scroll_end:
                scroll_start=scroll_end
                time.sleep(1)
                scroll_end=self.driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight); return arguments[0].scrollHeight',scroll_box_followers)
                if scroll_end==scroll_start:
                    time.sleep(5)
                    scroll_end=self.driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight); return arguments[0].scrollHeight',scroll_box_followers)
            else: break


        links=scroll_box_followers.find_elements_by_tag_name('a')
        names=[name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath(Constants.close_scroll_box).click()
        return names

    def get_following_list(self):
        self.driver.find_element_by_xpath(Constants.following_xpath.format(self.username)).click()

        scroll_box_followers=self.driver.find_element_by_xpath(Constants.scroll_box_xpath)
        
        scroll_start=0
        scroll_end=1

        while True:
            if scroll_start!=scroll_end:
                scroll_start=scroll_end
                time.sleep(1)
                scroll_end=self.driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight); return arguments[0].scrollHeight',scroll_box_followers)
                if scroll_end==scroll_start:
                    time.sleep(5)
                    scroll_end=self.driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight); return arguments[0].scrollHeight',scroll_box_followers)
            else: break
        
        links=scroll_box_followers.find_elements_by_tag_name('a')
        names=[name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath(Constants.close_scroll_box).click()
        return names
    
    def get_unfollowers(self):
        self.driver.find_element_by_xpath(Constants.profile_xpath.format(self.username)).click()

        followers=self.get_followers_list()
        following=self.get_following_list()

        unfollowers=[name for name in following if name not in followers]
        self.driver.quit()
        print("People who arnt following you %s:"%(unfollowers))





my_bot=InstaBot(Constants.username,Constants.password)
my_bot.get_unfollowers()
