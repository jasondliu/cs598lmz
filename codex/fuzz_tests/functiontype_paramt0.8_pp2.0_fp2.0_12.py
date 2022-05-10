from types import FunctionType
list(FunctionType(a(),b()))"""

    def test_list_iterable(self):
        self.assertCodeExecution(self.BASE_CODE)

    def test_list_none(self):
        self.assertCodeExecution(self.BASE_CODE + "\nlist(None)")

    def test_list_generator(self):
        self.assertCodeExecution(
            """
            def f():
                yield 1
                yield 2

            print(list(f()))
            """
        )

    def test_list_custom_object(self):
        self.assertCodeExecution(
            """
            class CustomObject:
                def __init__(self):
                    self.x = 2

                def __iter__(self):
                    return self

                def __next__(self):
                    self.x = self.x * 2
                    if self.x < 100:
                        return self.x
                    else:
                        raise StopIteration

            lst = list(CustomObject())
            print(lst)
            """
        )

    def test_
