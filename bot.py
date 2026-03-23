import random
import sys
import time
import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

# X 접속
driver.get("https://x.com")
time.sleep(5)

# 쿠키 로드
with open("cookies.pkl", "rb") as f:
    cookies = pickle.load(f)

for cookie in cookies:
    driver.add_cookie(cookie)

# 로그인된 상태로 이동
driver.get("https://x.com/home")
time.sleep(5)

# 트윗 작성 페이지
driver.get("https://x.com/compose/post")
time.sleep(5)

# 트윗 입력
tweet_box = driver.find_element(By.XPATH, "//div[@role='textbox']")
tweet_box.send_keys(tweet)
time.sleep(2)

# 트윗 버튼 클릭
tweet_button = driver.find_element(By.XPATH, "//button[@data-testid='tweetButton']")
tweet_button.click()

time.sleep(5)
driver.quit()

print("트윗 완료:", tweet)
