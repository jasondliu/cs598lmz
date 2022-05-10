gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
gi.gi_code
gi.gi_frame
# Test gi.gi_frame.f_locals and gi.gi_frame.f_globals
gi.gi_frame.f_locals
gi.gi_frame.f_globals

# Test that a generator is an iterator
isinstance(gi, collections.Iterator)

# Test that a generator is a context manager
with gi as i:
    pass

# Test that a generator is a coroutine
async def amain():
    async with gi as i:
        pass

# Test that a generator is a generator
def main():
    with gi as i:
        pass

# Test that a generator is an async iterator
async def amain():
    async for i in gi:
        pass

# Test that a generator is an async generator
async def amain():
    async with gi as i:
        pass


# Test that a generator is an iterator
isinstance(gi, collections.Iterator)

# Test that a generator is a context
