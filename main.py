from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 50
CHROME_DRIVER_PATH = "/usr/bin/chromedriver"
TWITTER_USERNAME = "YOURS"
TWITTER_PASSWORD = "YOURS"
SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/"

class InternetSpeedTwitterBot():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        print("initialized")

        self.down = 0
        self.up = 0
        self.down_unit = ""
        self.up_unit = ""
    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        print(SPEED_URL)
        time.sleep(3)
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        time.sleep(50)
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.down_unit = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[1]/span').text
        self.up_unit  = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[1]/span').text
        self.driver.minimize_window()

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(5)
        sign_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div')
        sign_in.click()

        time.sleep(20)

        user_name = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        user_name.send_keys(TWITTER_USERNAME)
        user_name.send_keys(Keys.ENTER)

        time.sleep(30)

        password = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(30)

        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Python Bot Tweet! #PythonBot/n my internet Uploads speed {self.up} {self.up_unit}, Downloads speed {self.down}"
                        f"{self.down_unit}")

        send_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        send_tweet.click()





check_speed = InternetSpeedTwitterBot()
print("test")
check_speed.get_internet_speed()
check_speed.tweet_at_provider()
