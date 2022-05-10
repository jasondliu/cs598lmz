import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import random


def get_random_demo_index() -> int:
    """Return a random demo index."""
    return random.randint(0, DEMO_LIST.__len__() - 1)


def get_demo(demo_index: int) -> Demo:
    """Return a demo from index."""
    if DEMO_LIST.__len__() <= demo_index:
        return False

    demo_data = DEMO_LIST[demo_index]
    return Demo(demo_data['name'], demo_data['link'], demo_data['duration'])


def get_demo_count() -> int:
    """Return count of demos in the list."""
    return DEMO_LIST.__len__()
