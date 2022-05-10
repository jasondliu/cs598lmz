import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(AbstractUser):
    # email = models.EmailField(max_length=254, unique=True)
    # username = models.CharField(max_length=254, unique=True)
    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=30, blank=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # last_login = models.DateTimeField(null=True, blank=True)
    # date_joined = models.DateTimeField(auto_now_add=True)
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']
    # objects = UserManager()


