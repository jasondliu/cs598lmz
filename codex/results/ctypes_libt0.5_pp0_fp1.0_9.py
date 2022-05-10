import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Twitter Login")

email = input("Email: ")
password = input("Password: ")

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://twitter.com/login")
time.sleep(2)

username = driver.find_element_by_name("session[username_or_email]")
username.send_keys(email)

pw = driver.find_element_by_name("session[password]")
pw.send_keys(password)

login = driver.find_element_by_xpath("//div[@role='button']")
login.click()

time.sleep(2)

ctypes.windll.kernel32.SetConsoleTitleW("Twitter Login - Success!")

print("Successfully logged in!")

time.sleep(2)

ctypes.windll.kernel32.SetConsoleTitleW("Twitter Login")

driver.quit()
