from selenium import webdriver
from selenium.webdriver.common.by import By
import os



PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = '/Users/admin/Development/chromedriver'
TWITTER_EMAIL = os.environ.get('TWITTER_EMAIL')
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')
SPEED_TEST_URL = 'https://www.speedtest.net/'


class InternetSpeedBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_upload_speed(self):
        return self.up

    def get_download_speed(self):
        return self.down

    def get_internet_speed(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        consent_button = self.driver.find_element(By.ID, '_evidon-banner-acceptbutton')
        consent_button.click()
        go_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        # go_button.click()
        # self.up = float(self.driver.find_element(By.CLASS_NAME, 'upload.speed'))
        # self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed'))


speed_test = InternetSpeedBot(CHROME_DRIVER_PATH)
print("Down before: ", speed_test.get_download_speed())
print("Up before: ", speed_test.get_upload_speed())
speed_test.get_internet_speed(SPEED_TEST_URL)
print("Down after: ", speed_test.get_download_speed())
print("Up after: ", speed_test.get_upload_speed())