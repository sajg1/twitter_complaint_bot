from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time



PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = '/Users/admin/Development/chromedriver'
TWITTER_EMAIL = os.environ.get('TWITTER_EMAIL')
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')
TWITTER_USERNAME = '@interne00336103'
SPEED_TEST_URL = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%' \
              '22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D'
PROVIDER = "my provider"


class InternetSpeedBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
        self.speed_test_url = 'https://www.speedtest.net/'

    def get_upload_speed(self):
        return self.up

    def get_download_speed(self):
        return self.down

    def get_internet_speed(self):
        self.driver.get(self.speed_test_url)
        self.driver.maximize_window()
        consent_button = self.driver.find_element(By.ID, '_evidon-banner-acceptbutton')
        consent_button.click()
        time.sleep(2)
        # DISMISS NOTIFICATION
        notification = self.driver.find_element(By.CLASS_NAME, 'notification-dismiss')
        notification.click()
        time.sleep(2)
        # COMMENCE SPEED TEST
        go_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go_button.click()
        time.sleep(50)
        # UPDATE UP AND DOWN FIGURES
        self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)
        self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)

    def tweet_at_provider(self, url, provider, promised_up, promised_down):
        self.get_internet_speed()
        if self.up < promised_up or self.down < promised_down:
            self.driver.get(url)
            self.driver.maximize_window()
            time.sleep(5)

            # ENTER EMAIL ADDRESS AND NEXT
            email_input = self.driver.find_element(By.NAME, 'text')
            email_input.send_keys(TWITTER_EMAIL)
            next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                                                             'div/div/div[2]/div[2]/div[1]/div/div[6]')
            next_button.click()
            # POSSIBLE 'UNUSUAL LOGIN ACTIVITY' PAGE
            try:
                time.sleep(3)
                username_input = self.driver.find_element(By.NAME, 'text')
                username_input.send_keys(TWITTER_USERNAME)
                next_button_2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/'
                                                                   'div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
                next_button_2.click()
            except NoSuchElementException:
                print("No unusual activiy page")
            # ENTER PASSWORD AND LOGIN
            time.sleep(5)
            password_input = self.driver.find_element(By.NAME, 'password')
            password_input.send_keys(TWITTER_PASSWORD)
            login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/'
                                                              'div/div/div[2]/div[2]/div[2]/div/div/div')
            login_button.click()

            tweet = f"Hey {provider}, why is my internet speed {self.down}down/{self.up}up when I pay for" \
                    f" {PROMISED_DOWN} down/{PROMISED_UP}up?"
            time.sleep(5)

            # WRITE AND SEND TWEET
            whats_happening_input = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
            whats_happening_input.send_keys(tweet)
            send_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div'
                                                            '/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]'
                                                            '/div/div/div[2]/div[3]')
            send_tweet.click()


speed_test = InternetSpeedBot(CHROME_DRIVER_PATH)
speed_test.tweet_at_provider(TWITTER_URL, PROVIDER, PROMISED_UP, PROMISED_DOWN)