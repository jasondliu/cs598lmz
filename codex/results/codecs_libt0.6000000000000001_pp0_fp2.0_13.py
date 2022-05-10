import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 打印日志
def print_log(msg):
    print(msg)
    sys.stdout.flush()

# 初始化数据库
def init_db():
    print_log('init_db')
    with app.app_context():
        db.drop_all()
        db.create_all()
        # 初始化超级管理员
        if not User.query.filter_by(id=1).first():
            admin = User(id=1, username='admin', password=generate_password_hash('123456'), is_admin=True)
            db.session.add(admin)
            db.session.commit()

# 创建命令行
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# 数据
