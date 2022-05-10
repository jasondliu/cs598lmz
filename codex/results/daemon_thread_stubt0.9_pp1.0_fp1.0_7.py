import sys, threading

def run():
    browser = webdriver.Firefox(options=options)
    browser.get('https://samples.openweathermap.org/data/2.5/history/city?q=Warren,OH&appid=b6907d289e10d714a6e88b30761fae22')
    browser.find_elements_by_xpath('//*[@id="history"]/div/div/table/tbody/tr/td')[1].text
    browser.find_elements_by_xpath('//*[@id="history"]/div/div/table/tbody/tr/td')[8].text

    print(browser.find_elements_by_xpath('//*[@id="history"]/div/div/table/tbody/tr/td')[1].text, end=" ")
    print(browser.find_elements_by_xpath('//*[@id="history"]/div/div/table/tbody/tr/td')[8].text)

while True:
    run()
</code>



