from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome(r'D:\chromedriver_win32\chromedriver.exe')
browser.get('https://animesoul.com/cards')
key = input()
search = browser.find_element_by_class_name('el_input_inner')
search.send_keys(key + Keys.RETURN)
