from bz2 import BZ2Decompressor
BZ2Decompressor.UNUSED_DATA = b''

import requests
import json

from .config import config
from . import module

@module.register('vk_group_posts', {
    'token': config.Get('vk_group_posts_token'),
    'group': config.Get('vk_group_posts_group'),
    'offset': config.Get('vk_group_posts_offset', 0),
    'count': config.Get('vk_group_posts_count', 10),
    'timeout': config.Get('vk_group_posts_timeout', 5),
})
class vk_group_posts(module.Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.posts = {}
        self.last_update = None

    def update(self):
        self.last_update = time.time()
        self.posts = json.loads(BZ2Decompressor().decompress(requests.get(
            'https://api.vk.com
