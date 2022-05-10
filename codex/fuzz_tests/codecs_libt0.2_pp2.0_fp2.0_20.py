import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=11)
    user_address = models.CharField(max_length=50)
    user_postcode = models.CharField(max_length=6)
    user_state = models.IntegerField(default=0)
    user_create_time = models.DateTimeField(auto_now_add=True)
    user_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

class Book(models.Model):
    book_id = models.AutoField(primary_key=
