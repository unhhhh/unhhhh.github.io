from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import re

playlist_url = 'https://www.youtube.com/playlist?list=PLhgFEi9aNUb2BNrIEecCGXApgeX7Yjwz8'

with open("api_key.txt", "r+") as file:
    api_key = file.read()

from pyyoutube import Api
api = Api(api_key="your api key")

driver = webdriver.Chrome()


# ---------------------------------
# get links from url
def get_links(driver, url, sleep_time):
    # https://stackoverflow.com/questions/63192583/get-youtube-playlist-urls-with-python#63192700
    # open driver window
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.get(url)

    # wait some seconds
    time.sleep(sleep_time)

    # get information from url
    soup = bs(driver.page_source, 'html.parser')
    res = soup.find_all('ytd-playlist-panel-video-renderer')

    # check if there is information
    if len(res) > 0:
        main_url = 'https://www.youtube.com/watch?v='
        urls = re.findall('watch.*list', str(res))
        links = [main_url + str(a[8:-9]) for a in urls[::2]]
    # if there is no information return false
    else:
        links = False
    return links


links = get_links(driver, playlist_url, 10)
