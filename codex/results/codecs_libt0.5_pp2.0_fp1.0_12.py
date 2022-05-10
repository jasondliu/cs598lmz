import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Create your models here.
class Resource(models.Model):
    resource_name = models.CharField(max_length=50)
    resource_type = models.CharField(max_length=50)
    resource_description = models.CharField(max_length=200)
    resource_url = models.CharField(max_length=200)
    resource_date = models.DateTimeField(auto_now_add=True)
    resource_author = models.CharField(max_length=50)
    resource_image = models.FileField(upload_to='resource_images/')
    resource_rating = models.IntegerField(default=0)
    resource_tags = models.CharField(max_length=200)
    resource_comments = models.CharField(max_length=500)

    def __unicode__(self):
        return self.resource_name

class Tag(models.Model):
    tag_name = models.CharField(
