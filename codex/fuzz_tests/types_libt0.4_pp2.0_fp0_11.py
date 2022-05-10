import types
types.MethodType(lambda self: self._get_value_or_default(self.name),
                 None,
                 models.Model)
</code>

