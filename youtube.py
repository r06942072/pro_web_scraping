import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get("https://www.youtube.com/")

search_bar = browser.find_element_by_id('search')
search_bar.send_keys('travel Taiwan')
search_bar.send_keys(Keys.ENTER)
#search_icon = browser.find_element_by_id('search-icon-legacy')
#search_icon.click()
time.sleep(3)
browser.get(browser.current_url)
time.sleep(3)

all_videos = browser.find_elements_by_id('video-title')
#all_videos = browser.find_elements_by_xpath('//*[@id="video-title"]')
#all_videos = browser.find_elements_by_tag_name('a')
for video in all_videos:
    video_url = video.get_attribute('href')
    video_ID = video_url.split('?v=')[-1]
    print(video_ID)

print("Finish youtube scraping")

'''
##right click and click "copy link address"
#actionChains = ActionChains(browser)
#actionChains.context_click(first_video).perform()
#time.sleep(3)
'''
