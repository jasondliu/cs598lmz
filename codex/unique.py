import glob
import logging
import shutil
import sys
import tqdm

def copy_unique(in_dir, out_dir):
    """Copy all unique tests in `in_dir` to `out_dir`."""
    unique = {}
    for path in tqdm.tqdm(glob.glob(f"{in_dir}/*"),
                          desc="Copying unique files"):
        with open(path, "r") as f:
            code = f.read()
        if code not in unique:
            unique[code] = path
            shutil.copy2(path, out_dir)
        else:
            logging.info(f"{path} is a duplicate of {unique[code]}")

def main(argv):
    if len(argv) <= 2:
        print(f"usage: {argv[0]} IN_DIR OUT_DIR")

    logging.basicConfig(filename=f"logs/unique.log", level=logging.INFO)
    in_dir = argv[1]
    out_dir = argv[2]
    copy_unique(in_dir, out_dir)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
