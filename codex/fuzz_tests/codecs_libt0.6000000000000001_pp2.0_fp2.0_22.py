import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 30, unique = True, blank = False)
    password = models.CharField(max_length = 30, blank = False)
    email = models.CharField(max_length = 30, blank = False)
    register_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    profile_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length = 30, blank = False)
    last_name = models.CharField(max_length = 30, blank =
