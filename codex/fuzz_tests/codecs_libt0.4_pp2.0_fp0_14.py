import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='user/')
    def __str__(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=30)
    pub_time = models.DateTimeField(auto_
