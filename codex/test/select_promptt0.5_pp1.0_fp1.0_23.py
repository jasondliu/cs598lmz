import select
# Test select.select()
#   - Check if select.select() blocks
#   - Check if select.select() raises an Exception
#   - Check if select.select() returns a list
#   - Check if select.select() returns the correct list

# Test select.select()
#   - Check if select.select() blocks
def test_select_blocks():
    # Setup
    r, w = os.pipe()
    # Exercise
    start_time = time.time()
    select.select([r], [], [])
    end_time = time.time()
    # Verify
    assert end_time - start_time > 0.1
    # Cleanup
    os.close(r)
    os.close(w)

# Test select.select()
#   - Check if select.select() raises an Exception
def test_select_raises_exception():
    # Setup
    r, w = os.pipe()
    os.close(r)
    os.close(w)
    # Exercise and Verify
