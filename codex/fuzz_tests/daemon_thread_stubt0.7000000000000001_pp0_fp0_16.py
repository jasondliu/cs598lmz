import sys, threading

def run():
    # 爬取页面
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.save_screenshot('baidu.png')
    driver.get_screenshot_as_file('baidu.png')
    driver.quit()


def main():
    # 开启多线程
    threads = []
    for i in range(1):
        threads.append(threading.Thread(target=run))
    for i in range(1):
        threads[i].start()


if __name__ == '__main__':
    main()
