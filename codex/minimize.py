import multiprocessing
import glob
import os
import shutil
import sys
import logging
import subprocess
import tempfile

import tqdm

TEST_FOLDER = 'test'
MINIMIZED_FOLDER = 'minimized'
LOG_FOLDER = 'logs'
os.makedirs(TEST_FOLDER, exist_ok=True)
os.makedirs(MINIMIZED_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

def ddmin_lines(name, expected, test_dir, output_dir):
    """Minimize a test in terms of lines. This deletes lines while ensuring
    the returncode of running `test` is `expected`."""
    with open(f"{test_dir}/{name}", "r") as f:
        code = [line for line in f]
    out_path = f"{output_dir}/{name}"

    def write_test(lines):
        nonlocal code, out_path
        with open(out_path, "w") as f:
            for line in lines:
                f.write(code[line])

    def test(lines):
        nonlocal cache, out_path, expected, name
        lines_tuple = tuple(lines)
        if lines_tuple in cache:
            return cache[lines_tuple]

        write_test(lines)

        try:
            cmd = ["python3", out_path]
            result = subprocess.run(cmd, timeout=5, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            if result.returncode == expected:
                ret = True
            else:
                ret = False
        except subprocess.TimeoutExpired:
            logging.info(f"{name}: timed out")
            ret = False

        cache[lines_tuple] = ret
        return ret

    def check_subsets(subsets):
        for s in subsets:
            if test(s):
                return (True, s)
        return (False, None)

    lines = [i for i in range(len(code))]
    cache = {}
    n = 2
    while True:
        size = max(1, -(-len(lines) // n))
        deltas = []
        nablas = []
        for i in range(n):
            start = i * size
            end = start + size
            deltas.append(lines[start:end])
            nablas.append(lines[:start] + lines[end:])

        reduced, delta = check_subsets(deltas)
        if reduced:
            n = 2
            lines = delta
            continue

        reduced, nabla = check_subsets(nablas)
        if reduced:
            n = max(n - 1, 2)
            lines = nabla
            continue

        if n < len(lines):
            n = min(len(lines), n * 2)
        else:
            break

    logging.info(f"minimized {name}; line count {len(code)} -> {len(lines)}")
    write_test(lines)

class Minimizer:
    def __init__(self, test_dir, output_dir):
        self.test_dir = test_dir
        self.output_dir = output_dir

    def __call__(self, t):
        ddmin_lines(t[0], t[1], self.test_dir, self.output_dir)

def minimize_crash_tests(output_path):
    """Minimize all crashing tests in `output_path`."""
    crashing_tests = []
    with open(output_path, "r") as f:
        for line in f:
            fields = line.split(" ")
            if fields[1] == "crash":
                crashing_tests.append((fields[0], -int(fields[2])))

    with tempfile.TemporaryDirectory() as tmpdir:
        base = os.getcwd()
        os.chdir(tmpdir)
        with multiprocessing.Pool() as pool:
            m = Minimizer(f"{base}/{TEST_FOLDER}", f"{base}/{MINIMIZED_FOLDER}")
            for t in tqdm.tqdm(pool.imap_unordered(m, crashing_tests),
                               total=len(crashing_tests), desc="Minimizing"):
                pass

def main(argv):
    logging.basicConfig(filename=f"{LOG_FOLDER}/minimize.log", level=logging.INFO)
    minimize_crash_tests("output")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
