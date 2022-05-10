import sys, threading

def run():
    # set up Python interpreter state
    sys.path.append(os.getcwd())
    sys.path.append(os.path.join(os.getcwd(), 'lib'))
    sys.path.append(os.path.join(os.getcwd(), 'src'))
    sys.path.append(os.path.join(os.getcwd(), 'src', 'web'))
    # set up django
    import django.core.management
    django.core.management.setup_environ(project.settings)
    import django.conf
    django.conf.settings.LOGGING_CONFIG_FILE = os.path.join(os.getcwd(), 'src', 'web', 'logging.conf')
    import logging.config
    logging.config.fileConfig(django.conf.settings.LOGGING_CONFIG_FILE)
    # run django
    django.core.management.call_command(sys.argv[1], *sys.argv[2:])

if __name__ == "__main
