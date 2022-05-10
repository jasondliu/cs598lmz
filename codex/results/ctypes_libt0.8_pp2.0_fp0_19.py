import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
Browser automatization
<code>def create_profile(profile_path):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    options.add_argument(f'--user-data-dir={profile_path}')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument(f'--disk-cache-dir={profile_path}')
    options.add_argument(f'--app=file://{profile_path}')

    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
