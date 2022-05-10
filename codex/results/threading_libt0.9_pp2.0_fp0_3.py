import threading
threading._DummyThread._Thread__stop = lambda x: 0

from pyon.util.log import log
from pyon.util.array_util import ArrayUtil
from pyon.ion.process import SimpleProcess
from pyon.public import RT
from pyon.net.endpoint import RPCServer
from pyon.net.transport import NameTrio
from pyon.net.messaging import make_message_headers
from pyon.util.int_test import IonIntegrationTestCase
from pyon.util.containers import DotDict
from pyon.event.event import EventSubscriber, EventPublisher, EventAgent
from ion.services.dm.utility.granule.record_dictionary import RecordDictionaryTool


class EventIntegrationTest(IonIntegrationTestCase):

    event_list = []

    def setUp(self):
        self._start_container()
        self.container.start_rel_from_url('res/deploy/r2deploy.yml')
        self.event_list = []
        # self.receiver = Receiver("receiver",
