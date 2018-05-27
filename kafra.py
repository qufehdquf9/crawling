from selenium import webdriver

driver = webdriver.Chrome('/Users/choi/Downloads/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('http://kafra.kr/#!/ko/KRO/itemdeal/0//1')

search = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/section[1]/div/div/form/div/input')
search.click()
search.send_keys('')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/section[1]/div/div/form/div/span/input').click()