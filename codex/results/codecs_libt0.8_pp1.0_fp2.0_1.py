import codecs
codecs.register(lambda name: Codecs(name, "windows-1252"))

# TODO Makefile isomorphism

# TODO Makefile variables

# TODO Makefile functions

# TODO Makefile syntax

# TODO Makefile recursive make

# TODO Makefile parallel make

# TODO Makefile parallel make
#       + $(MAKE) -jN

class Makefile(object):
    def __new__(cls, path, *args, **kwargs):
        """
        :param path: ``Path`` to the ``Makefile``
        """
        for fmt in cls.formats:
            if fmt.match(path):
                # TODO: Mypy optimization?
                return fmt(path, *args, **kwargs)
        raise ValueError(path)

    def __iter__(self):
        """
        Iterate over ``Target`` names
        :return: ``Target`` names
        :rtype: ``str``
        """
        for k in self.targets.keys():
            yield k

    def __getitem__
