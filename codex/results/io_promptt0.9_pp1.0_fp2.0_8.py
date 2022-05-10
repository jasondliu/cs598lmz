import io
# Test io.RawIOBase.readinto() method.
io.RawIOBase.readinto(None)
io.RawIOBase.readinto()

# Test io.RawIOBase.readinto() method.
io.BufferedIOBase.readinto(None)
io.BufferedIOBase.readinto()
""")

  def test_incorrect_inheritance(self):
    ty = self.Infer("""
      import StringIO
      class MyIO(StringIO.StringIO):
        pass
      x = MyIO()
      y=x.read()
    """)
    self.assertOnlyHasReturnType(ty.Lookup("y"), self.str)

    ty = self.Infer("""
      import StringIO
      class MyIO(StringIO.StringIO):
        pass
      x = MyIO()
      y=x.readline()
    """)
    self.assertOnlyHasReturnType(ty.Lookup("y"), self.str)

    ty = self.Infer("""
      import StringIO
      class MyIO(StringIO.StringIO):
        pass
