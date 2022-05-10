import types
types.ModuleType.x = "test!"

def export_var(self, name, value):
    setattr(self, name, value)

types.ModuleType.export_var = export_var
