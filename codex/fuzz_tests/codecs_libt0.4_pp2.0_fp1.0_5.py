import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_birth = models.CharField(max_length=100)
    user_sex = models.CharField(max_length=100)
    user_point = models.IntegerField(default=0)
    user_level = models.IntegerField(default=0)
    user_join_date = models.DateTimeField(default=timezone.now)
    user_last_login = models.DateTimeField(default=timezone
