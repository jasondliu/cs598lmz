import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 가상환경에서 돌리기 위한 설정
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from faker import Faker
from blog.models import Post


# Post 모델을 생성하는 함수
def create_posts(N):
    fake = Faker()
    for _ in range(N):
        title = fake.sentence()
        content = fake.text()
        created_at = fake.date_time_this_year()
        post = Post.objects.create(title=title, content=content, created_at=created_at)


# 실행
if __name__ == '__main__
