import select
# Test select.select()

def testSelect():
    print("testing select.select()")
    assert select.select([], [], [], 0.0) == ([], [], []), "select.select() returned incorrect data"
    print("passed")

testSelect()
