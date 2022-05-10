from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__builtins__', '__file__', '__name__', '__package__', '__doc__', '__loader__', '__spec__', '__annotations__', '__all__', '__version__', '__author__', '__email__', '__license__', '__copyright__', '__title__', '__summary__', '__uri__', '__keywords__', '__classifiers__', '__requires__', '__provides__', '__obsoletes__', '__platforms__', '__requires_dist__', '__provides_dist__', '__obsoletes_dist__', '__requires_external__', '__project_urls__', '__entry_points__', '__extras_require__', '__python_requires__', '__install_requires__', '__setup_requires__', '__tests_require__', '__test_suite__', '__test_loader__', '__test_runner__', '__zip_safe__', '
