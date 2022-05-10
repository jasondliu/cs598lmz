import _struct

SIG_EXT = '.sig'

# TODO(vincent): store the signature of the file
#                in a separate file.
# TODO(vincent): add a .sig file in the zip file.
#                this signature must be verified as well.

def _sign(file_name, pad_size, key_file_name, key_size):
    """
    Sign and write the signature at the end of the file.
    """
    with open(file_name, 'ab') as f:
        f.write(_struct.pack('<I', 0))
        f.write(os.urandom(pad_size))
    if key_file_name:
        subprocess.check_call(('openssl', 'dgst', '-sha1',
                              '-sign', key_file_name,
                              '-keyform', 'DER',
                              '-out', file_name + SIG_EXT,
                              file_name))
