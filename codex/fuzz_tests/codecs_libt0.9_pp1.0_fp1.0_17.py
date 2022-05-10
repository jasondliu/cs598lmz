import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 登录
def loging(u):
    print('用户: ', u.name)
    wd = u.wd
    driver = wd.getDriver()
    logout(wd)
    wd.timeSleep(3)
    driver.find_element_by_xpath(u.LOGIN_URL).click()
    wd.timeSleep(2)
    driver.find_element_by_xpath(u.LOGIN_USER).send_keys(u.name)
    wd.timeSleep(1)
    driver.find_element_by_xpath(u.LOGIN_PASSWORD).send_keys(u.password)
    wd.timeSleep(1)
    driver.find_element_by_xpath(u.LOGIN_BUTTON).click()
    wd.timeSleep(2)
    if driver.find_element_by_xpath(u.LOGIN_USER).
