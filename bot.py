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

# 랜덤 실행 (약 1~2시간 간격 느낌)
if random.random() < 0.5:
    print("이번 실행 스킵")
    sys.exit()

# 트윗 문장 랜덤 선택
with open("tweet.txt", "r", encoding="utf-8") as f:
    tweets = f.readlines()

tweet = random.choice(tweets).strip()

# 크롬 옵션 (헤드리스)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# 트위터 로그인 페이지
driver.get("https://twitter.com/i/flow/login")
time.sleep(7)

# 아이디 입력
username_input = driver.find_element(By.XPATH, "//input[@autocomplete='username']")
username_input.send_keys(USERNAME)
username_input.send_keys(Keys.ENTER)
time.sleep(5)

# 비밀번호 입력
password_input = driver.find_element(By.XPATH, "//input[@name='password']")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(7)

# 트윗 작성 페이지 이동
driver.get("https://twitter.com/compose/tweet")
time.sleep(7)

# 트윗 입력
tweet_box = driver.find_element(By.XPATH, "//div[@aria-label='Tweet text']")
tweet_box.send_keys(tweet)
time.sleep(3)

# 트윗 버튼 클릭
tweet_button = driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
tweet_button.click()

time.sleep(5)
driver.quit()

print("트윗 완료:", tweet)
