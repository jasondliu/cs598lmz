import codecs
codecs.register_error("strict", codecs.ignore_errors)

def includeme(config):
    """Including Pyramid requests and views."""
    # Pyramid request
    config.add_request_method(get_user, 'user', reify=True)
    config.add_request_method(get_flash, 'flash', reify=True)
