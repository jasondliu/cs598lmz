import select
# Test select.select() with an invalid timeout
select.select( [], [], [], None )
