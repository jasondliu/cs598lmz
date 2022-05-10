import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

class Message:
    """
    Message class for parsing and storing information of message
    """
    def __init__(self, message):
        """
        :param message: message that needs to be parsed
        """
        self.message = message
        self.message_id = message['id']
        self.user_id = message['from']['id']
        self.text = message['text']
        self.first_name = message['from']['first_name']
        self.last_name = message['from']['last_name']
        self.username = message['from']['username']
        self.chat_id = message['chat']['id']
        self.chat_title = message['chat']['title']
        self.chat_username = message['chat']['username']
        self.date = message['date']


class TelegramBot(telepot.Bot):
    """
    TelegramBot class for specifying all the callbacks for messages on telegram
    """
    def
