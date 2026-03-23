import random
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = os.environ['TWITTER_USERNAME']
PASSWORD = os.environ['TWITTER_PASSWORD']

# 랜덤 실행 (1~2시간 느낌)
if random.random() < 0.5:
    print("이번 실행 스킵")
    sys.exit()

# 트윗 문장 랜덤 선택
with open("tweet.txt", "r", encoding="utf-8") as f:
    tweets = f.readlines()

tweet = random.choice(tweets)

# 크롬 옵션 (헤드리스)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# 트위터 로그인
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

# 트윗 작성
tweet_box = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tweet text']")
tweet_box.send_keys(tweet)
time.sleep(2)

tweet_button = driver.find_element(By.XPATH, "//span[text()='Tweet']")
tweet_button.click()

time.sleep(5)
driver.quit()
