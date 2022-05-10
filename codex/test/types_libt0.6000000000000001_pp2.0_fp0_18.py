import types
types.ModuleType = ModuleType


class Module(ModuleType):
    __getattr__ = getattr
    __setattr__ = setattr
    __delattr__ = delattr
    __dir__ = dir

    def __init__(
        self,
        name: str,
        doc: str,
        *,
        version: str,
        author: str,
        license: str,
        homepage: str,
        description: str,
        long_description: str,
        long_description_content_type: str,
        keywords: str,
        package_dir: str,
        package_data: str,
        packages: str,
        zip_safe: str,
        install_requires: str,
        python_requires: str,
        classifiers: str,
        entry_points: str,
    ):
        super().__init__(name)
        self.__name__ = name
        self.__doc__ = doc

        self.version = version
        self.author = author
        self.license = license
        self.homepage = homepage
