import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_input(path):
    with open(path) as f:
        return f.read()

def get_output(path):
    with codecs.open(path, encoding='utf-8', errors='strict') as f:
        return f.read()

def run_test(path):
    input = get_input(path)
    output = get_output(path)
    result = process(input)
    if result != output:
        print('Failed {}'.format(path))
        print('Expected:')
        print(output)
        print('Got:')
        print(result)
        return False
    return True

def main():
    for path in sorted(glob.glob('test_cases/*.in')):
        if not run_test(path):
            return 1
    print('All tests passed!')
    return 0

if __name__ == '__main__':
    sys.exit(main())
