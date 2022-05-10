import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'school',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    # execute_from_command_line(sys.argv)  # 当使用命令行时，会先判断属性类型
    manage.run()
