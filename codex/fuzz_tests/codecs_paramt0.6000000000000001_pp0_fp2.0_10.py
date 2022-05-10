import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='E-mail')
    text = models.TextField(verbose_name='Текст сообщения')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('-date_added',)
