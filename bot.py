import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = os.environ['TWITTER_USERNAME']
PASSWORD = os.environ['TWITTER_PASSWORD']

with open("tweet.txt", "r", encoding="utf-8") as f:
    tweets = f.readlines()

tweet = random.choice(tweets)

driver = webdriver.Chrome()

driver.get("https://twitter.com/login")
time.sleep(5)

username_input = driver.find_element(By.NAME, "text")
username_input.send_keys(USERNAME)
username_input.send_keys(Keys.ENTER)
time.sleep(3)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(5)

tweet_box = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tweet text']")
tweet_box.send_keys(tweet)
time.sleep(2)

tweet_button = driver.find_element(By.XPATH, "//span[text()='Tweet']")
tweet_button.click()

time.sleep(5)
driver.quit()