import types
types.SimpleNamespace

'''
Attributes:
    req - the req (request) object to be logged
    res - the res (response) object to be logged
    err - any error that needs to be logged
    prod_name - any production name you want to make available in log output
    custom_msg - if you need to pass your own message in a data field
    req_user - if you have created a user object, this will be the format in the log
'''
template = {
    'req': '',
    'res': '',
    'err': '',
    'prod_name': '',
    'custom_msg': '',
    'req_user': ''
}


class Logger:

    def __init__(self, logger_name=None, config=None, api_info=None, namespace=template):

        self.namespace = namespace
        self.logger_name = logger_name
        self.config = config
        self.api_info = api_info

