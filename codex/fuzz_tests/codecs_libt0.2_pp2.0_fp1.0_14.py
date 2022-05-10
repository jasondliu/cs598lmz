import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_address = models.CharField(max_length=50)
    user_postcode = models.CharField(max_length=50)
    user_sex = models.CharField(max_length=50)
    user_birthday = models.DateField()
    user_regtime = models.DateTimeField()
    user_status = models.IntegerField()
    user_isadmin = models.IntegerField()
    user_image = models.CharField(max_length=50)
    user_nickname = models.
