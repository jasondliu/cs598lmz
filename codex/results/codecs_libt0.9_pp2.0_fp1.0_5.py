import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

app.jinja_env.filters['zip'] = zip

if platform.system() != 'Darwin':
    # monkey.patch_all()  # 打开, 线程会阻塞
    pass

# 初始化全局变量
CACHE = dict()

CACHE['PY_VERSION'] = platform.python_version()
CACHE['GO_VERSION'] = (check_output(['go', 'version'])).decode()
CACHE['PROJECT_NAME'] = 'ganji'
CACHE['COMMIT'] = (check_output(['git', 'rev-parse', 'HEAD'])).decode().strip('\n')
CACHE['TAG'] = (check_output(['git', 'tag'])).decode()
CACHE['BRANCH'] = (check_output(['git', 'rev-parse',
