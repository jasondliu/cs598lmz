import threading
threading._DummyThread._Thread__stop = lambda x: 42

# convenience function
def _get_type_string(t):
    """
    returns a string representing a type in the format of
    'type_name (type_id)'
    """
    if isinstance(t, pydrizzle.drizzle.DrizzleType):
        t = t.id
    identifier = pydrizzle.drizzle.DrizzleType.id2name(t)
    if identifier is None:
        identifier = "Unknown"
    return "%s (0x%02x)" % (identifier, t)

# convenience function
def _get_option_string(o):
    """
    returns a string representing an option in the format of
    'option_name (option_id)'
    """
    if isinstance(o, pydrizzle.drizzle.DrizzleOption):
        o = o.id
    identifier = pydrizzle.drizzle.DrizzleOption.id2name(o)
    if identifier is None:
        identifier = "Unknown"
    return "%s (0
