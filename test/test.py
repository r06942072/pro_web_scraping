from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.seleniumhq.org/")

# click() simulate clicking
elem_download = browser.find_element_by_link_text("Download")
elem_download.click()

# send_keys() simulate typing
searchBar = browser.find_element_by_id('q')
searchBar.send_keys('download')

# Keys.ENTER simulate hitting ENTER on Keyboard
searchBar.send_keys(Keys.ENTER)
