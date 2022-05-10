import select
# Test select.select with "select" first parameter set to ""
# It is an error, but it should not segfault, see issue #15845
select.select("", [], [], 0)
select.select([], "", [], 0)
select.select([], [], "", 0)
