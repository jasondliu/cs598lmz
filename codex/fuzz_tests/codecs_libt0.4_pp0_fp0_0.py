import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=11)
    user_address = models.CharField(max_length=100)
    user_postcode = models.CharField(max_length=6)
    user_grade = models.IntegerField()
    user_sex = models.CharField(max_length=1)
    user_birthday = models.DateField()
    user_regtime = models.DateTimeField(auto_now_add=True)
    user_status = models.IntegerField()
    user_head = models.ImageField(upload_to='head', default='head/default.jpg')

