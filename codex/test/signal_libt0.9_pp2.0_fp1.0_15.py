import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)


def execute(compiler, source_path, pass_name, compilation_database=False,
            allow_extra_args=False):
    print('%s: source: %s' % (pass_name, source_path), file=sys.stderr)
    compiler = shlex.split(compiler)
    if compilation_database:
        compiler.extend(shlex.split(
            '-Xclang -load -Xclang %s/%s.so -Xclang -add-plugin -Xclang remove-unreachable-passes' %
            (os.environ['LLVM_BUILD_DIR'],
             'LLVMRemoveUnreachablePassesPPCallbacks')))
    else:
        compiler.extend(shlex.split('-plugin %s/LLVMPassPPCallbacks.so' %
                                    os.environ['LLVM_BUILD_DIR']))
