import _struct_bbox_pb2
import _struct_bbox_pb2_grpc
import logging

from .factory import factory


class StructBboxServicer(object):
    def __init__(self):
        self._handler = factory.get_struct_bbox_handler()

    def GetStructBbox(self, request, context):
        try:
            request = _struct_bbox_pb2.StructBboxRequest.FromString(request.SerializeToString())
            res = self._handler.get_struct_bbox(request)
            return _struct_bbox_pb2.StructBboxResponse.FromString(res.SerializeToString())
        except Exception as e:
            logging.error('Get struct bbox failed.\n{}'.format(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Get struct bbox failed.\n{}'.format(e))


def serve(max_workers=None, port=None):
    parser = argparse.ArgumentParser()
    parser
