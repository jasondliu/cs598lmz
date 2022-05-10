import threading
threading.Semaphore()._Semaphore__value
import datamodel


def func(number):
    count = 100 / number

    try:
        os.mkdir('data')
    except FileExistsError:
        pass

    for i in range(count):
        f = open('data/input1.txt', 'w')
        number = random.randint(0, 500)
        f.write(str(number))
        f.close()

        with open('data/input2.txt') as data_file:
            data_json = json.load(data_file)

        model = datamodel.MyModel()
        result = model.get_data()
        print(result)


if __name__ == '__main__':
    t1 = threading.Thread(target=func, args=(3, ))
    t2 = threading.Thread(target=func, args=(5, ))
    t3 = threading.Thread(target=func, args=(7, ))
