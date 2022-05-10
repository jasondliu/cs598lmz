import codecs
# Test codecs.register_error()
import sys
import tempfile
import unittest
import warnings


def get_codecs():
    write_support = []
    read_support = []
    non_working = set()
    for name in codecs.__all__ + ['utf-8-sig']:
        if name in non_working:
            continue
        try:
            if '.' in name:
                encoding = name
                name = ''
            else:
                encoding = name + ':'
            c = codecs.lookup(encoding)
            try:
                encoder = c.encode('')
                if encoder:
                    s = encoder.encode('\xff')
                    write_support.append((c, name, encoding))
                else:
                    write_support.append((c, name, encoding + " (no incremental encoder)"))
            except Exception:
                non_working.add(name)
            try:
                decoder = c.decode(b'')
                if decoder:
                    decoder.decode(b'\xff')
                   
