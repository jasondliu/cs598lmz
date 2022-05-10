import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_address = models.CharField(max_length=50)
    user_city = models.CharField(max_length=50)
    user_state = models.CharField(max_length=50)
    user_zip = models.CharField(max_length=50)
    user_country = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    user_status = models.CharField(max_length=50)
    user_created_date =
