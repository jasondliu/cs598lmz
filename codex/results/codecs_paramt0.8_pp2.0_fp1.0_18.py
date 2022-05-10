import codecs
codecs.register_error('strict', codecs.ignore_errors)

import subprocess

import numpy as np

import get_phonemes
import get_utils


def main():
    options = get_utils.get_options()
    if options.name is None:
        name = "tmp"
    else:
        name = options.name

    utils_opts = get_utils.UtilsOpts(options.words, options.phones, options.output_dir, name)

    utils_opts.check_output()
    get_phonemes.main(utils_opts)


if __name__ == '__main__':
    main()
