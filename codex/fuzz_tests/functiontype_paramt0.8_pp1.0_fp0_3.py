from types import FunctionType
list(FunctionType(lambda x: None, {}).__code__.co_names)

for param in params:
    print(param)
    for i in range(1, 11):
        measurement = []
        for j in range(10):
            print(j)
            r = requests.get('http://192.168.1.102:8080/api/v1/request_route', params=param)
            data = r.json()
            measurement.append((data['result']['travelTime'], data['result']['moved']))

        # x, y = zip(*measurement)
        # x = [i/1000 for i in x]
        measurement = [i[0]/1000 for i in measurement]
        print(measurement)
        print(sum(measurement)/len(measurement))
        res.append(measurement)
        time.sleep(10)

# with open('test.txt', 'w') as file:
#     for i in range(len(res)):
#         row = res[i]
#         for j
