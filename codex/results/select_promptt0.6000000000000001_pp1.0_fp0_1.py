import select
# Test select.select with a selectable from the file module.
import file
import time

def callback(source, condition):
    print source, condition

select.select([file.File("/dev/null", "r")], [], [], 1.0)
select.select([file.File("/dev/null", "r")], [], [], 1.0, callback)

select.select([file.File("/dev/null", "r")], [], [], 1.0)
select.select([file.File("/dev/null", "r")], [], [], 1.0, callback)

select.select([file.File("/dev/null", "r")], [], [], 1.0)
select.select([file.File("/dev/null", "r")], [], [], 1.0, callback)

select.select([file.File("/dev/null", "r")], [], [], 1.0)
select.select([file.File("/dev/null", "r")], [], [], 1.0, callback)

select.select
