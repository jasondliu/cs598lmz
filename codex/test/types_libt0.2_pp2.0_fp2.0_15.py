import types
types.MethodType(lambda self: self.get_absolute_url(), Post)

# Добавляем метод в класс
Post.get_absolute_url = lambda self: reverse('post_detail', args=[self.id])

# Вызываем метод
Post.get_absolute_url(post)

# Проверяем что метод добавился в класс
Post.get_absolute_url

# Проверяем что метод добавился в объект
post.get_absolute_url

