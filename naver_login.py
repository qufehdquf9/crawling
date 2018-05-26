from selenium import webdriver

driver = webdriver.Chrome('/Users/choi/Downloads/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://nid.naver.com/nidlogin.login')
#id/passward 입력
driver.find_element_by_name('id').send_keys('naver_id')
driver.find_element_by_name('pw').send_keys('naver_passward')
# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()