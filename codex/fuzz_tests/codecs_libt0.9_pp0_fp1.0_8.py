import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

def ReadTxt():    

    dataType = ['Region', 'Country', 'Item Type', 'Sales Channel', 'Order Priority', 'Order Date', 'Order ID', 'Ship Date', 'Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']
    data = open('orders.txt', 'r', encoding='cp65001')
    dataorder = open('ordered.txt', 'w')
    writer = csv.writer(dataorder, delimiter=',')        
    reader = csv.reader(data)
    order = []
    for i in range(13):
        order.append(0)
    writer.writerow(order)

    index = 0
    while True:
        line = data.readline()
        if not line:
            break
        index += 1
        line = line.split(',')

        if line[1] == 'Region':
            order[0] = index
        elif line
