import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class WpFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post
        django_get_or_create = ('title', 'slug')

    title = 'Lorm ipsum'
    wp_title = 'Lorm ipsum'
    slug = 'lorem-ipsum'
    content = '<p>lorem ipsum</p>'


class PostTestCases(TestCase):
    def test_wp_published_posts_from_factory_create(self):
        post = WpFactory.create()
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__unicode__(), u'lorem ipsum')

class PostTests(TestCase):
    def setUp(self):
        self.post = Post(title='lorem ipsum', content='<p>lorem ipsum</p>')
        self.post
