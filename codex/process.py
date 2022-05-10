import re
import sys

class InvalidRecordError(Exception):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return f"Invalid input {repr(self.line)}"

class Record:
    def __init__(self, line):
        try:
            fields = line.split()
            self.name = fields[0]
            self.type = fields[1]
            self.signal = fields[2]
            self.n_deleted = fields[3]
            self.has_name_error = fields[4]
            self.test_lines = fields[5]
        except IndexError:
            raise InvalidRecordError(line)

        m = re.match("(.+)(lib|prompt|param|stub)t([0-9.]+)_pp([0-9.]+)_fp([0-9.]+)_[0-9]+.py", self.name)
        if m:
            self.prompt_name = m.group(1)
            self.prompt_type = m.group(2)
            self.temp = m.group(3)
            self.pp = m.group(4)
            self.fp = m.group(5)
        else:
            raise InvalidRecordError(line)


def process_output(output_path):
    counts = {}
    with open(output_path, "r") as f:
        next(f)
        for line in f:
            rec = Record(line)

            if rec.prompt_type not in counts:
                counts[rec.prompt_type] = {"before": {}, "after": {}}

            d = counts[rec.prompt_type]["before"]
            if int(rec.n_deleted) > 0:
                if "error" not in d:
                    d["error"] = 0
                d["error"] += 1
            else:
                if rec.type not in d:
                    d[rec.type] = 0
                d[rec.type] += 1
            d = counts[rec.prompt_type]["after"]
            if rec.type not in d:
                d[rec.type] = 0
            d[rec.type] += 1

    cols = ["lib", "prompt", "param", "stub"]
    rows = ["crash", "error", "pass", "timeout"]
    col_max = max(map(len, cols))
    row_max = max(map(len, rows))
    fmt = f"{{:<{row_max}}}" + f"{{:>{col_max}}} " * len(cols)
    print(fmt.format("Before", *cols))
    sums = [0] * len(cols)
    for r in rows:
        sums = map(lambda t: t[0] + t[1], zip(sums, [counts[c]["before"].get(r, 0) for c in cols]))
        print(fmt.format(r, *(counts[c]["before"].get(r, 0) for c in cols)))
    print(fmt.format("total", *sums))

    print()
    rows = ["crash", "empty", "pass", "timeout"]
    print(fmt.format("After", *cols))
    sums = [0] * len(cols)
    for r in rows:
        sums = map(lambda t: t[0] + t[1], zip(sums, [counts[c]["after"].get(r, 0) for c in cols]))
        print(fmt.format(r, *(counts[c]["after"].get(r, 0) for c in cols)))
    print(fmt.format("total", *sums))


def main(argv):
    process_output("merged_output")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
