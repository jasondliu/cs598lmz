import types
types.MethodType(lambda self: self.get_queryset().filter(is_active=True),
                 User.objects, User)
</code>

