import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

class Home(BaseHandler):
    def get(self):
        return self.render('home.html')

class MainPage(BaseHandler):
    def get(self):
        return self.render('main.html')

class Login(Auth):
    def get(self):
        return self.render('login.html')

    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        if username and password:
            re = self.db.get("SELECT * FROM user WHERE username = %s and password = %s",username,password)
            if re:
                self.set_secure_cookie("username", username)
                self.set_secure_cookie("userid", str(re.id))
                self.redirect("/main")
            else:
                self.redirect("/login")
        else:
            self.redirect("/login")

class Register
