import _struct
# Test _struct.Struct

def test_struct():
    struct = _struct.Struct('bBhHiIlLqQfdspP')
    fmt = 'bbHHhhiIlLqQfdfsP'
    for i in range(256):
        for j in range(256):
            for k in range(65536):
                for l in range(65536):
                    for m in range(65536):
                        for n in range(65536):
                            for o in range(65536):
                                for p in range(65536):
                                    for q in range(65536):
                                        for r in range(65536):
                                            for s in range(65536):
                                                for t in range(65536):
                                                    for u in range(65536):
                                                        for v in range(65536):
                                                            for w in range(65536):
                                                                for x in range(65536):
                                                                    for y in range(65536):
                                                                        for z in range(65536):
                                                                            for a
