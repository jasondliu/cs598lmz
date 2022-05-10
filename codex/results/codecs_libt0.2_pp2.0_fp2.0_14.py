import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=20)
    user_postcode = models.CharField(max_length=20)
    user_sex = models.CharField(max_length=20)
    user_birthday = models.CharField(max_length=20)
    user_image = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20)
    user_regtime
