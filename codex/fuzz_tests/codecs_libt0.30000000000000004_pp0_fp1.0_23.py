import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=20)
    user_birthday = models.DateField()
    user_gender = models.CharField(max_length=20)
    user_image = models.CharField(max_length=200)
    user_register_date = models.DateTimeField()
    user_status = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20)

    def __str__(self):

