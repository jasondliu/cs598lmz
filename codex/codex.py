
'''
to address max length, maybe just delete the last line (or continue to delete until no SyntaxError)
better not to install third-party libraries

TODO
1. concatenate the prompt and completion
2. collect more seeds
    e.g., remove parameters, pre-add the library and functions (we can compare the effectiveness / results of different extraction strategies)
    the collected buggy code could be used to fine-tune
3. do more extensive experiments
    codex parameter tuning, multiple runs (seems random seeds is not controllable)
    how many of the generated code are syntax correct code?
    line of coverage of interpreter?
4. maybe different max_len and larger temperature?
'''


'''
to run the script:

nohup python -u codex.py > logs/codex_$(date "+%m.%d-%H.%M.%S").log &
'''

import os
import sys
import time
import logging
import traceback
import subprocess

import numpy as np
import openai

from os import listdir
from os.path import isfile, join
from timeit import default_timer as timer

from logger import init_log


with open('codex_api_key', 'r') as f:
    openai.api_key = f.read().strip()

INPUT_FOLDER = 'inputs'
RESULT_FOLDER = 'results'
LOG_FOLDER = 'logs'
os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

N = 25 # generate N completions for each prompt, it does not affect API rate limit


def main():

    log_path = os.path.join(LOG_FOLDER, 'main')
    init_log(log_path, level=logging.DEBUG)

    files = [f for f in listdir(INPUT_FOLDER) if isfile(join(INPUT_FOLDER, f))]

    for filename in files:
        complete_code_from_prompt(filename)



def complete_code_from_prompt(filename):
    prompt = read_prompt(filename)

    '''https://beta.openai.com/docs/api-reference/completions'''
    idx = filename.find('.py')

    # temperature: Higher values means the model will take more risks. Try 0.9 for more creative applications,
    # and 0 (argmax sampling) for ones with a well-defined answer.
    # Seems 0.9 are more likely to generate syntax incorrect code. but 0 would produce the same result for every run?
    # for temp in np.arange(0, 1, 0.1):
    for temp in np.arange(0, 1, 0.1):
        for presence_penalty in [0, 1.0, 2.0]:
            for frequency_penalty in [0, 1.0, 2.0]:
                tmp_name = filename[:idx] + f't{temp}_pp{presence_penalty}_fp{frequency_penalty}' + '_24.py'
                tmp_name = os.path.join(RESULT_FOLDER, tmp_name)
                if os.path.exists(tmp_name):
                    logging.debug(f'{tmp_name} already exists')
                else:
                    try:
                        s1 = timer()
                        response = openai.Completion.create(
                        engine="code-davinci-002",
                        prompt=prompt,
                        temperature=temp,
                        max_tokens=256,
                        top_p=1,
                        n=N,
                        echo=True,
                        frequency_penalty=0,
                        presence_penalty=0)

                        try:
                            for i in range(N):
                                x = response['choices'][i]['text']
                                name = filename[:idx] + f't{temp}_pp{presence_penalty}_fp{frequency_penalty}' + '_' + str(i) + '.py'
                                result_file = os.path.join(RESULT_FOLDER, name)
                                with open(result_file, 'w') as f:
                                    f.write(x + '\n')
                            # TODO: run separately
                            # run_generated_code(result_file)
                        except:
                            logging.error(f'{filename} t{temp}_pp{presence_penalty}_fp{frequency_penalty} error ' + \
                                        traceback.format_exc())

                        s2 = timer()
                        diff = s2 - s1
                        logging.debug(f'diff: {diff}')
                        if diff < 4:
                            time.sleep(4 - diff)
                    except:
                        logging.error(f'{filename} t{temp}_pp{presence_penalty}_fp{frequency_penalty} need to rerun')
                        time.sleep(60)


def read_prompt(filename):
    input_file = os.path.join(INPUT_FOLDER, filename)
    with open(input_file, 'r') as f:
        prompt = f.read().strip()
    return prompt


def delete_last_line(path):
    """Delete the last line of the file at `path`. Return whether the file is
    non-empty after this deletion."""
    with open(path, "rb+") as f:
        f.seek(-1, os.SEEK_END) # skip the last char (it's probably a newline)
        pos = f.tell()
        while pos > 0 and f.read(1) != b'\n':
            f.seek(-1, os.SEEK_CUR)
            pos -= 1
        f.truncate()
        return pos > 0


def run_generated_code(result_file):
    # TODO copy instead of overwriting
    while True:
        cmd = ['python', result_file]
        result = subprocess.run(cmd, stderr=subprocess.PIPE)
        if result.returncode < 0: # some signal
            # you can match the specific signal here, e.g.,
            # if result.returncode == -signal.SIGSEGV:
            #     print("segv")
            logging.info(f"{result_file}: test crashed with signal {-result.returncode}")
            return
        elif result.returncode > 0: # some error
            last = result.stderr.decode().rstrip().splitlines()[-1]
            if "SyntaxError" in last:
                if delete_last_line(result_file):
                    continue
                else:
                    logging.error(f"{result_file}: reduced to empty file")
                    return


if __name__ == '__main__':
    t1 = timer()
    main()
    t2 = timer()
    logging.info(f'time elapsed: {t2 - t1:.1f} seconds')
