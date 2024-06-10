import time
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode for faster execution
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL of T-Series on Dailymotion
url = "https://www.dailymotion.com/tseries2"

# Open the page
driver.get(url)
time.sleep(3)  # Wait for the page to load

# Scroll and collect video URLs
video_urls = set()
while len(video_urls) < 500:
    elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/video/")]')
    for elem in elements:
        href = elem.get_attribute('href')
        if href and "/video/" in href:
            video_urls.add(href)
        if len(video_urls) >= 500:
            break
    # Scroll down to load more videos
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

driver.quit()

# Extract video IDs from URLs
video_ids = [url.split('/video/')[1] for url in video_urls]

# Count frequency of characters in video IDs
char_counter = Counter("".join(video_ids).lower())

# Find the most frequent character
most_common_char, most_common_count = sorted(char_counter.items(), key=lambda x: (-x[1], x[0]))[0]

# Print the result in the expected format
print(f"{most_common_char}:{most_common_count}")
