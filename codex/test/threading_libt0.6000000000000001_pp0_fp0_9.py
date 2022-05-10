import threading
threading.Thread(target=lambda: selenium.webdriver.Chrome(chrome_options=chrome_options)).start()

import time
time.sleep(2)

# 웹사이트 접속
driver.get('https://www.facebook.com')

# 해당 웹사이트가 로딩될 때까지 기다리기
time.sleep(3)

# id, pw입력
driver.find_element_by_name('email').send_keys('id')
driver.find_element_by_name('pass').send_keys('pw')

# 로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="u_0_2"]').click()

# 해당 웹사이트가 로
