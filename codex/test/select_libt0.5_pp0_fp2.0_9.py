import select
import sys
import time
import tty

from . import base


class Keypress(base.Base):
  """Watches stdin for keypresses.

  Example:

    from grr.lib import flags
    from grr.lib.aff4_objects import collects
    from grr.lib.flows.general import processes

    flags.FLAGS.debug = True

    # Run the flow on the client.
    for _ in test_lib.TestFlowHelper(
        "Keypress",
        client_mock.MockClient(),
        token=self.token,
        output="analysis/keypress"):
      pass

    # Read the output.
    fd = aff4.FACTORY.Open(
        client_id.Add("analysis/keypress"), token=self.token)
    print fd.Get(fd.Schema.STORED)

  """

  def Start(self):
    """The flow starts."""
    self.state.Register("output", self.output.Add("stored"))
