from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome(r'D:\chromedriver_win32\chromedriver.exe')
browser.get('https://animesoul.com/cards')
key = input() 
search = browser.find_element_by_class_name('el-input__inner')
search.send_keys(key + Keys.RETURN)
tier_div = browser.find_element_by_class_name('el-dropdown')
s_tier = input()
if s_tier == 'Tier 1':
  options = tier_div.find_elements_by_xpath("//li[contains(text(), 'Tier 1')]")
elif s_tier == 'Tier 2':
  options = tier_div.find_elements_by_xpath("//li[contains(text(), 'Tier 2')]")
elif s_tier == 'Tier 3':
  options = tier_div.find_elements_by_xpath("//li[contains(text(), 'Tier 3')]")
elif s_tier == 'Tier 4':
  options = tier_div.find_elements_by_xpath("//li[contains(text(), 'Tier 4')]")
elif s_tier == 'Tier 5':
  options = tier_div.find_elements_by_xpath("//li[contains(text(), 'Tier 5')]")
elif s_tier == 'Tier 6':
  options = tier_div.find_elements_by_xpath("//li[contains(text(), 'Tier 6')]")
else:
  options = tier_div.find_elements_by_xpath("//li[contains(text(), 'All')]")
tier_div.click()
for value in options:
  value.click()
c_link_div = browser.find_element_by_class_name('card-main')
c_link_div.click()
c_url = browser.current_url

