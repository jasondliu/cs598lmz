import weakref

class User(object):
    def __init__(self, id, name, password=None, phone=None, email=None,
                 gender=None, birthday=None, pic=None, country=None,
                 province=None, city=None, lat=None, lon=None, addr=None,
                 confirm=None, last_login=None, create_at=None,
                 update_at=None, updater=None):
        self.id = id
        self.name = name
        self.password = password
        self.phone = phone
        self.email = email
        self.gender = gender
        self.birthday = birthday
        self.pic = pic
        self.country = country
        self.province = province
        self.city = city
        self.lat = lat
        self.lon = lon
        self.addr = addr
        self.confirm = confirm
        self.last_login = last_login
        self.create_at = create_at
        self.update_at = update_at
        self.updater = upd
