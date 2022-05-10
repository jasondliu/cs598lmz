gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom

# Test iterating over gi
for i in gi:
    print(i)

# Test gi.__next__
gi.__next__()

# Test gi.send
gi.send(None)

# Test gi.throw
gi.throw(ValueError)

# Test gi.close
gi.close()

# Test gi.__await__
gi.__await__()

# Test gi.__aiter__
gi.__aiter__()

# Test gi.asend
gi.asend(None)

# Test gi.athrow
gi.athrow(ValueError)

# Test gi.aclose
gi.aclose()

# Test gi.ag__await__
gi.ag__await__()

# Test gi.ag
