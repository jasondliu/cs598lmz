import codecs
# Test codecs.register_error to handle JSONDecodeError: Expecting value: line 1 column 1 (char 0)
codecs.register_error('strict', json.decoder.JSONDecodeError, json.JSONDecoder.raw_decode)
#codecs.register_error('strict', json.decoder.JSONDecodeError, json.decoder)

def config_matrix():
    return {
        'engine' : {
                    'lxf' : 'file', # rawshare_engine_lxf.py
                    'raw' : 'http', # rawshare_engine_http.py
                    'img' : 'file', # rawshare_engine_img.py
                    'json' : 'file', # rawshare_engine_json.py
                    'prj' : 'file', # rawshare_engine_prj.py
                   },
        'wire' : {
                   'memcached' : 'memcached', # rawshare_wire_memcached.py
                   'redis' : 'redis', # rawshare_wire_redis.py
                   'file' : '
