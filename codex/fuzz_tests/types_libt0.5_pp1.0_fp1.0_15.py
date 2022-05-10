import types
types.ModuleType.__getattr__ = lambda self, name: self.__dict__[name]

if __name__ == '__main__':
    main()
