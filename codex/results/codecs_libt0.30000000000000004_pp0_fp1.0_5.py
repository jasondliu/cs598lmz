import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Goods(models.Model):
    goodsname = models.CharField(max_length=50)
    goodsprice = models.IntegerField()
    goodsnum = models.IntegerField()
    goodsimage = models.CharField(max_length=50)
    goodsinfo = models.CharField(max_length=50)
    goodsaddress = models.CharField(max_length=50)
    goodstype
