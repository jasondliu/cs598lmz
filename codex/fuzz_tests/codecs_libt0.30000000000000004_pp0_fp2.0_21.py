import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=100)
    user_birth = models.CharField(max_length=20)
    user_gender = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20)
    user_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id

class User_Info(models.Model):
    user_id =
