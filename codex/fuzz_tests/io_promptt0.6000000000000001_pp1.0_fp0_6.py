import io
# Test io.RawIOBase

print(issubclass(io.RawIOBase, io.IOBase))

import io
# Test io.BufferedIOBase

print(issubclass(io.BufferedIOBase, io.IOBase))

import io
# Test io.TextIOBase

print(issubclass(io.TextIOBase, io.IOBase))

import io
# Test io.StringIO

print(issubclass(io.StringIO, io.TextIOBase))

import io
# Test io.BytesIO

print(issubclass(io.BytesIO, io.BufferedIOBase))

import io
# Test io.TextIOWrapper

print(issubclass(io.TextIOWrapper, io.TextIOBase))

import io
# Test io.FileIO

print(issubclass(io.FileIO, io.RawIOBase))

import io
# Test io.BufferedReader

print(issubclass(io.BufferedReader, io.BufferedIOBase))

import io
# Test io.BufferedWriter
