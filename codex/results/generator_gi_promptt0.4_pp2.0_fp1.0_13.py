gi = (i for i in ())
# Test gi.gi_code
# print(gi.gi_code)

# Test gi.gi_frame
# def foo():
#     yield 1
#     yield 2
# gi = foo()
# print(gi.gi_frame)

# Test gi.gi_running
# def foo():
#     yield 1
#     yield 2
# gi = foo()
# print(gi.gi_running)
# next(gi)
# print(gi.gi_running)
# next(gi)
# print(gi.gi_running)

# Test gi.gi_yieldfrom
# def foo():
#     yield from range(5)
# gi = foo()
# print(gi.gi_yieldfrom)
# next(gi)
# print(gi.gi_yieldfrom)
# next(gi)
# print(gi.gi_yieldfrom)

# Test gi.send(None)
# def foo():
#     print('Starting')
#     while True:
#         res = yield 4
#         print('res:', res)
#
