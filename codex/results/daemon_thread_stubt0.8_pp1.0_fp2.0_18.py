import sys, threading

def run():
    from model_mommy import mommy
    from django.contrib.auth import get_user_model
    from django.contrib.auth.management import create_permissions

    User = get_user_model()
    User.objects.get_or_create(email=config.EMAIL_ADMIN)
    User.objects.get_or_create(email=config.EMAIL_CLIENT)

def main():
    path = os.getcwd()
    if 'bin' in path:
        path += '/..'

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
    sys.path.append(path)

    from django.core.management 
