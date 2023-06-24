from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "YOUR DRIVER PATH"
ig_username = "YourInstaID"
ig_pass = "PASSWORD"
target_account = "FOLLOWING ACCOUNT"

class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        username = self.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        username.send_keys(ig_username)
        password = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password.send_keys(ig_pass)
        password.send_keys(Keys.ENTER)
        time.sleep(4)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{target_account}/")
        time.sleep(4)
        followers = self.driver.find_element(By.XPATH, '//a[@href="/{target_account}/followers/"]/span')
        followers.click()
        time.sleep(4)

    def follow(self):
        for num in range(1, 20):
            time.sleep(2)
            follow_button = self.driver.find_element(By.XPATH, f'//button[text()="Follow"]')
            if follow_button.text == "Follow":
                follow_button.click()
            else:
                pass
            time.sleep(1)

    def run(self):
        self.login()
        self.find_followers()
        self.follow()
        self.driver.quit()

bot = InstaFollower(chrome_driver_path)
bot.run()
