import multiprocessing
import glob
import os
import shutil
import sys
import logging
import subprocess
import tempfile
from functools import partial

import tqdm

RESULT_FOLDER = 'results'
TEST_FOLDER = 'test'
LOG_FOLDER = 'logs'
os.makedirs(RESULT_FOLDER, exist_ok=True)
os.makedirs(TEST_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

def delete_last_line(path):
    """Delete the last line of the file at `path`. Return whether the file is
    non-empty after this deletion."""
    with open(path, "r+") as f:
        text = [line for line in f]
        text = text[:-1]
        f.seek(0)
        f.write("".join(text))
        f.truncate()
        return bool(text)

class TestResult:
    def __init__(self, name):
        self.name = name   # filename of test
        self.type = "pass" # type of test result
        self.signal = 0    # signal if this was a crash
        self.n_deleted = 0 # number of lines deleted
        self.has_name_error = False # whether a name error was ever seen
        self.test_lines = 0 # length of this test

def run_generated_code(result_file, test_dir):
    """Run `result_file` and return what happened."""
    name = result_file.rsplit("/", 1)[1]
    copy_path = f"{test_dir}/{name}"
    shutil.copyfile(result_file, copy_path)

    ret = TestResult(name)

    # skip temperature 0 tests, except for 0 0 0

    while True:
        cmd = ['python3', copy_path]
        try:
            result = subprocess.run(cmd, timeout=30, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        except subprocess.TimeoutExpired:
            #logging.info(f"{copy_path}: timed out")
            ret.type = "timeout"
            break
        if result.returncode < 0: # some signal
            # you can match the specific signal here, e.g.,
            # if result.returncode == -signal.SIGSEGV:
            #     print("segv")
            #logging.info(f"{copy_path}: test crashed with signal {-result.returncode}")
            ret.type = "crash"
            ret.signal = -result.returncode
            break
        elif result.returncode > 0: # some error
            try:
                last = result.stderr.decode().rstrip().splitlines()[-1]
                if "NameError" in last:
                    ret.has_name_error = True
            except:
                pass
            #logging.info(f"{copy_path}: error {last}")
            ret.n_deleted += 1
            if delete_last_line(copy_path):
                continue
            else:
                #logging.error(f"{copy_path}: reduced to empty file")
                ret.type = "empty"
                break
        else:
            break

    with open(copy_path, "r") as f:
        for line in f:
            ret.test_lines += 1
    return ret

def run_all_tests(out_file="output"):
    with tempfile.TemporaryDirectory() as tmpdir:
        base = os.getcwd()
        os.chdir(tmpdir)

        run_test = partial(run_generated_code,
                           test_dir=f"{base}/{TEST_FOLDER}")

        files = glob.glob(f"{base}/{RESULT_FOLDER}/*.py")
        with open(f"{base}/{out_file}", "w") as f:
            f.write("name type signal n_deleted has_name_error test_lines\n")
            with multiprocessing.Pool() as pool:
                for r in tqdm.tqdm(pool.imap_unordered(run_test, files),
                                   total=len(files), desc="Running tests"):
                    f.write(f"{r.name} {r.type} {r.signal} {r.n_deleted} {r.has_name_error} {r.test_lines}\n")

def main(argv):
    run_all_tests()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
