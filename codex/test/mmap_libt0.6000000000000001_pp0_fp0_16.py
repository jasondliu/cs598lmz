import mmap
import grpc.beta._stubs
import grpc.beta._interfaces

from grpc.beta import implementations


# _ONE_DAY_IN_SECONDS = 60 * 60 * 24

class ImageSearcher(object):
    def __init__(self, host='0.0.0.0', port='50051'):
        self.host = host
        self.port = port
        self.channel = implementations.insecure_channel(self.host, int(self.port))
        self.stub = beta_implementations.imagesearcher_pb2_grpc.ImageSearcherStub(self.channel)

    def Search(self, img_path):
        request = beta_implementations.imagesearcher_pb2.SearchRequest()
        request.img_path = img_path
        return self.stub.Search(request, 5.0)  # 5 secs timeout


def main():
    searcher = ImageSearcher()
    response = searcher.Search('/home/buxizhizhoum/1.jpg')
