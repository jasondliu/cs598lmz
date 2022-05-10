import bz2
bz2.__doc__
 
```

## Transforming and Reducing Data at the Same Time

### Example 1: Calculate total sales for each item

```python
sales = [('Apple', 'iphone3gs', 5000),
         ('Apple', 'ipad1',   12000),
         ('HTC',   'htc-hero',  4500),
         ('Apple', 'iphone6s', 10000),
         ('Apple', 'ipad2',   15000),
         ('HTC',   'htc-one',  13000),
        ]

# Without using map, reduce, and filter

apple_sales = 0
for s in sales:
    if s[0] == 'Apple':
        apple_sales += s[2]
        
print('Apple Sales: ', apple_sales)

htc_sales = 0
for s in sales:
    if s[0] == 'HTC':
        htc_sales += s[2]
        
print('HTC Sales: ', htc_sales)

```

