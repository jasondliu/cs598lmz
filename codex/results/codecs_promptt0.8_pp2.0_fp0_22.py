import codecs
# Test codecs.register_error('get-identity', codecs.get_identity_error);
# "fake" codecs module to test module-level functions
import encodings.ascii
ASCIIEncoding = encodings.ascii.Encoding
encodings.ascii.Encoding = None
import encodings.base64_codec
Base64Codec = encodings.base64_codec.Codec
encodings.base64_codec.Codec = None
import encodings.big5
Big5 = encodings.big5.Big5Codec
encodings.big5.Big5Codec = None
import encodings.big5hkscs
Big5HKSCS = encodings.big5hkscs.Big5HKSCSCodec
encodings.big5hkscs.Big5HKSCSCodec = None
import encodings.charmap
CharMapCodec = encodings.charmap.Codec
encodings.charmap.Codec = None
import encodings.cp037
CP037
