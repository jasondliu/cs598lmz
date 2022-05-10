import select
# Test select.select with selectors

sys.platform.startswith("sunos")
select.select([], [], [], 0)
select.select([], [], [], 0.25)
select.select([], [], [], 15)
select.select([], [], [], 10)

select.select([], [], [], -1)
select.select([], [], [], -2)
