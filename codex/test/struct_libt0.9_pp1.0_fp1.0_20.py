import _struct
import _random
import _gzip


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(message=""):
    print(message, end="")
    input(" { Hit enter to continue } ")


def sub_array(values, indices, dim=1):
    if dim == 1:
        return [values[i] for i in indices]
    elif dim == 2:
        return [[values[i][j] for j in indices] for i in indices]
    elif dim == 3:
        return [[[values[i][j][k] for k in indices]
                 for j in indices]
                for i in indices]


def write_csv(data, filename, header=""):
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        try:
            writer.writerow(header)
        except:
            pass
        for d in data:
            writer.writerow(d)


