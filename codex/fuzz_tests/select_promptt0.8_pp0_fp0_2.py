import select
# Test select.select() for passing in an empty list for the first argument.
# This is a regression test for SF bug 566347:
# http://sourceforge.net/tracker/index.php?func=detail&aid=566347&group_id=5470&atid=105470
select.select([], [], [])
