from types import FunctionType
list(FunctionType(lambda: True, {}).__code__.co_varnames)

# ['<lambda>']

# but this is not OK:
list(lambda: True.__code__.co_varnames)

# ['True']
```

The reason for this is that `lambda: True` is not a function,
but a `Lambda` instance.

## Known issues

There is currently no support for function annotations.

## Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
