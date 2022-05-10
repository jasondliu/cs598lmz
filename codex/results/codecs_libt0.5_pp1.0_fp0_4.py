import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    # profile_img = models.ImageField(upload_to='images/', default='images/default_profile.png')
    # profile_img = models.ImageField(upload_to='images/', default='images/default_profile.png')
    # profile_img = models.ImageField(upload_to='images/')
    profile_img = models.ImageField(upload_to='images/', default='images/default_profile.png')
    # profile_img = models.ImageField(upload_to='images/')
    # profile_img = models.ImageField(upload_to='images/', default='images/default_profile.png')
    # profile_img
