import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=100)
    user_postcode = models.CharField(max_length=20)
    user_date = models.DateTimeField(auto_now_add=True)
    user_point = models.IntegerField()
    user_grade = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to='images/', null=
