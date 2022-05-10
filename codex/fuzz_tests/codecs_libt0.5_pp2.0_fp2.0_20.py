import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    user_email = models.CharField(max_length=45)
    user_password = models.CharField(max_length=45)
    user_phone = models.CharField(max_length=45)
    user_address = models.CharField(max_length=45)
    user_created_date = models.DateTimeField(auto_now_add=True)
    user_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'User'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=45)
    category_created_date = models.Date
