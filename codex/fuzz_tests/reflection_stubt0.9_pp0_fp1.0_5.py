fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
with self.AssertRaisesRegex(ValueError, "co_code must be a string or a read-only buffer, not 'generator'"):
  base.create_module_namespace(fn)


class ModuleTest(vm_test_base.VmTestBaseWithFilesystem):

  def setUp(self):
    super(ModuleTest, self).setUp()
    self.module_namespace = {}
    self.running_module = None

  def construct_module(self, definitons):
    """Creates a test Module.

    Creates a test module that contains the specified named functions, classes,
    and variables (constants, etc., or both).

    Args:
      definitions: A mapping from identifier string to the global identifier
        that was assigned to it.

    Returns:
      A Module instance for the constructed module.
    """
    members = []
    for name, member in definitons.items():
      members.append(common.define_source(name, inspect.getsource(member)))
    members_source = '\n'.join(members
