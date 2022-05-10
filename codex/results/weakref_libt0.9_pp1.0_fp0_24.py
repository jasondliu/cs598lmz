import weakref

from pyp2rpm import exceptions, settings


def jsonpath_normalize(value):
    """
    The upstream bugfix releases contains bugfix chars in the version
    eg 1.3.1.dev-1 -> 1.3.1.dev1,
    they still follow the PEP 440
    specification, however an issue can occur, when the release
    with this package is eg f21, which has the same bug, so pyp2rpm
    won't be able to find the release, this fixes this.
    """
    if isinstance(value, str) and value.endswith("."):
        return value.strip(".")
    return value


def match(template, actual):
    """Test, if the actual version matches the version template
    from the duplicate section.

    If the actual version is eg 1.3.1.dev-1, bt template is 1.3.1,
    this would match. Same for v1.1 vs 1.1.

    :param Actual: instance of :py:class:`packaging.version.Version`
        or `StrictVersion
