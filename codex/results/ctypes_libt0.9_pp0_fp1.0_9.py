import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

df.to_excel('result.xlsx', sheet_name='Sheet_name_1')
 
# Google search to a new browser window
with open('material/a_.csv', encoding='utf-8') as f:
    adr = f.readlines()
adr = [x.strip() for x in adr]
driver = webdriver.Chrome()
driver.get('https://google.com')

for num,ad in enumerate(adr):
    print(num, ad)
    elem = driver.find_element_by_name('q')
    elem.click()
    elem.clear()
    elem.send_keys(ad)
    driver.find_element_by_name('btnK').click()


# Google search to a new browser window
adr = ['apple', 'google', 'facebook']
driver = webdriver.Chrome()
driver.get('https://google.com')

for ad in adr:
    print(
