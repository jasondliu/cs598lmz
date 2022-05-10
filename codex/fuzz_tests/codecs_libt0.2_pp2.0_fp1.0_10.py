import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20, unique=True)
    user_password = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=50, unique=True)
    user_phone = models.CharField(max_length=20, unique=True)
    user_address = models.CharField(max_length=50)
    user_gender = models.CharField(max_length=10)
    user_birthday = models.DateField()
    user_register_time = models.DateTimeField(auto_now_add=True)
    user_last_login_time = models.DateTimeField(auto_now=True)
    user_status = models.IntegerField(default=1)
    user_type = models.IntegerField
