import types
types.ClassType = None

def add_layout(layout_cfg):
    if layout_cfg.id in layouts:
        raise ValueError('Overwriting layout %s' % layout_cfg.id)
    layouts[layout_cfg.id] = Layout(layout_cfg)


def get_layout(layout_id):
    if layout_id not in layouts:
        return None
    return layouts[layout_id]


def get_layout_cfg(layout_id):
    layout = get_layout(layout_id)
    if layout is not None:
        return layout.layout_cfg
    return None


def get_layout_ids():
    return layouts.keys()


@property
def default_layout_id():
    return config.get('common', 'default_layout')


def add_window(window_cfg):
    if window_cfg.id in windows:
        raise ValueError('Overwriting window %s' % window_cfg.id)
    windows[window_cfg.id] = Window(window_cfg)


def get_window(window_id):
    if
