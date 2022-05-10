import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Plugin(BasePlugin):
    __name__ = 'sms'
    __version__ = '0.1'
    __description__ = 'This plugin sends SMS messages to a number'
    __author__ = 'Bastian Schroll'
    __author_mail__ = 'bastian@schroll.name'
    __license__ = 'GPL3'
    __date__ = '2013-12-08'
    __api__ = 1
    __priority__ = 'normal'
    __config__ = [
        {
            'name': 'sms_gateway',
            'type': 'str',
            'description': 'SMS gateway URL',
            'default': 'http://smsgateway.me/api/v3/messages/send',
        },
        {
            'name': 'sms_email',
            'type': 'str',
            'description': 'SMS gateway email',
            'default': '',
        },
        {
            'name': 'sms_password',
            '
