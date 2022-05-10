import _struct

log = logging.getLogger(__name__)


class DataSource(object):
    """
    Class that defines a datasource, from which a flow comes from,
    where the flows are saved to, and where the flows are sourced from.
    """

    def __init__(self, name):
        """
        Initialise the datasource.

        :param name: The name of the datasource.
        """

        self.name = name

    def get_flows(self):
        """
        Get the flows from the datasource.

        :return: The flows.
        """

        raise NotImplementedError

    def save_flows(self, flows):
        """
        Save the given flows to the datasource.

        :param flows: The flows to be saved.
        """

        raise NotImplementedError

