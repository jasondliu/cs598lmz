import select_time

class Login_page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.kuaiqiangche.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_login(self):
        u"""用户登录"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_css_selector("li.top-login > a.login-btn").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("13000000000")
        driver.find_element_by_id
