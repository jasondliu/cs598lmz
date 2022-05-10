import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_address = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    user_status = models.CharField(max_length=50)
    user_last_login = models.DateTimeField(auto_now_add=True)
    user_reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_
