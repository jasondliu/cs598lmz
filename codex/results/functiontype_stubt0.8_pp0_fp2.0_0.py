from types import FunctionType
a = (x for x in [1])
b = [x + 1 for x in a]

b

print(type(b))

class InstrumentImport:
    import_name = ''
    import_description = ''
    method = None
    def __init__(self, name, desc="", import_method=None):
        self.import_name = name
        self.import_description = desc
        self.method = import_method
    def __call__(self, func):
        self.method = func
        return func

class ImportManager(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_import(self, import_name, import_description, import_method):
        self.update({import_name: InstrumentImport(import_name, import_description)})

imports = ImportManager()

"""
@imports.add_import("firehose_local_1", "Firehose local data import", None)
def load_firehose_local_1(user_name):
    return None
"""


