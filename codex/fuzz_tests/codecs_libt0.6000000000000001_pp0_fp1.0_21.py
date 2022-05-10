import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# %%

def get_insta(insta, username, password, hashtag, max_pic_num, save_dir):
    """
    insta: webdriver
    username: your instagram account
    password: your instagram password
    hashtag: the hashtag you want to download
    max_pic_num: maximum number of pictures you want to download
    save_dir: the directory you want to save the pictures
    """
    insta.get('https://www.instagram.com/')
    time.sleep(2)
    insta.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
    insta.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
    insta.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(4)
    insta.find_element_by
