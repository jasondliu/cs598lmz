import io
# Test io.RawIOBase compatibility:
class TestRawIOBase(io.RawIOBase):
    ...
class TestBytesIO(io.BytesIO):
    ...
if __name__ == '__main__':
    sys.exit(0)
" > fake_io.py

dvdemux_ts_extra_libraries=$1
test_stream_encryption=$2

# Build unit tests for libyami
cd ./unittests
[ -e Makefile ] && make clean > /dev/null 2>&1
LD_LIBRARY_PATH=../build/../../${source_path}/libyami:${dvdemux_ts_extra_libraries} ./autogen.sh --host=${host_tag} --prefix=$PWD/build --with-test-crypto=${test_stream_encryption} --with-gi-typelib-path=../build/../../${source_path}/libyami
LD_LIBRARY_PATH=../build/../../${source_path}/libyami:${dvdemux_ts_extra_libraries
