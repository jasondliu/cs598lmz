import mmapi
import mm
import logging

logger = logging.getLogger()


class MMClient(object):
    """
    This is a client for a Mattermost server.  It allows for logging in,
    creating and joining channels, and sending messages.
    """

    def __init__(self, server, team, email, password, debug=False):
        """
        Constructor

        :param server: The server to connect to.
        :type server: str
        :param team: The team to log into.
        :type team: str
        :param email: The email of the user to log in as.
        :type email: str
        :param password: The password of the user to log in as.
        :type password: str
        :param debug: Enable debug logging.
        :type debug: bool
        """
        self.api = mmapi.API(
            server=server,
            team=team,
            email=email,
            password=password,
            debug=debug,
        )
        self.server = server
        self.team = team
        self.
