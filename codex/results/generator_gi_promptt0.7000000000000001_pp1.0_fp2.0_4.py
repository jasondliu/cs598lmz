gi = (i for i in ())
# Test gi.gi_code
gi.gi_code

# Test gi.gi_frame
gi.gi_frame

# Test gi.gi_running
gi.gi_running

# Test gi.gi_yieldfrom with gi_frame
gi = (i for i in range(10))
gi.gi_frame
gi.gi_yieldfrom

# Test gi.gi_yieldfrom with gi_frame
gi = (i for i in ())
gi.gi_frame
gi.gi_yieldfrom

# Test gi.gi_await with gi_frame
async def main():
    return

gi = main().__await__()
gi.gi_frame
gi.gi_await

# Test gi.gi_await with gi_frame
gi = ()
gi.gi_frame
gi.gi_await
