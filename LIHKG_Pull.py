from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import emoji
from selenium.webdriver.chrome.options import Options

WINDOW_SIZE = "1920,1080"
#
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

chromedriver_path = '/Users/ato/Downloads/chromedriver' # Change this to your own chromedriver path!
# webdriver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
webdriver = webdriver.Chrome(executable_path=chromedriver_path)


name_list=[]
try:
    for n in range(1,5):
        webdriver.get(f'https://lihkg.com/thread/2026101/page/{n}')
        sleep(10)
        for i in range(1,25):
            a = (n-1)*25+i
            commenter = webdriver.find_element_by_xpath(f'//*[@id="{a}"]/div/small/span[2]/a').text
            name_list.append(commenter)
except:
    pass

print(name_list)


