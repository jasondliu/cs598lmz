import weakref


__all__ = (
    'Action', 'Container', 'Group', 'ActionCollection', 'ActionCollectionUI',
    'ActionBase', 'ActionBaseUI', 'ActionBaseCollection', 'ActionBaseCollectionUI',
)


class Action(ActionBase):
    """
    This class holds information about an action.

    :param name:        the name of the action, must be unique
    :param label:       the text shown to the user
    :param tooltip:     the tooltip shown to the user.
    :param icon:        an icon to use as the action's icon.
    :param statustip:   the status tip shown in the status bar.
    :param checkable:   if True, the action will have a checkbox next to it.
    :param checked:     the state of the checkbox.
    :param enabled:     the action will be enabled if this is True.
    :param visible:     the action will be visible if this is True.
    :param separator:   if True, a separator is drawn before the action.
    :param shortcut:    a shortcut for the action
    :
