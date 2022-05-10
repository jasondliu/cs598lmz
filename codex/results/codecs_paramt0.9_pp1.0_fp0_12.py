import codecs
codecs.register_error("strict", codecs.ignore_errors)
title_to_url = {}

def get_url(title):
    return "http://www.encyclopedia-titanica.org" + title_to_url[title]

def get_data(title, attr):
    browser.get(get_url(title))
    elem = browser.find_element_by_id("ctl00_phMainContent_ctl00_DataList1")
    elems = list(iter(elem))
    attr_elem = elems[attr]
    return attr_elem.text

def get_data_all(title):
    raw = {}
    raw["given_name"] = get_data(title, 0)
    raw["surname"] = get_data(title, 1)
    raw["sex"] = get_data(title, 2)
    raw["age"] = get_data(title, 3)
    raw["survived"] = get_data(title, 4)
    raw["status_ticket"] = get_data(title, 5
