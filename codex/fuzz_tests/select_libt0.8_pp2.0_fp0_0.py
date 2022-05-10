import selectors
import json

class WebRequestHandler():

    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.data = None
        self.method = str(request.method).lower()
        self.headers = {x[0]:x[1] for x in self.request.headers}
        self.url_parts = request.uri.split("?")
        self.args = {}
        self.validate_method()
        self.validate_content_type()
        self.get_args()
        self.validate_args()
        self.fetch_data()

    def validate_method(self):
        if self.method not in ["get", "post", "delete", "put"]:
            raise web.HTTPError(405)

    def validate_content_type(self):
        if self.method not in ["delete"]:
            content_type = self.headers.get("content-type", "application/json")
            if content_type != "application/json":
                raise web.HTTPError(400
