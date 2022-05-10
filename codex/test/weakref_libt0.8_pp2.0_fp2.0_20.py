import weakref

class Generic(object):
    def __init__(self, *args, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name']
        elif len(args) > 0:
            self.name = args[0]
        else:
            raise Exception("Expected name")

        if 'description' in kwargs:
            self.description = kwargs['description']
        else:
            self.description = ""

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    def __repr__(self):
        return "%s" % self.name

class Character(Generic):
    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)

        if 'inventory' in kwargs:
            self.inventory = kwargs['inventory']
        else:
            self.inventory = {}
        self.inventory_ref = {}

