from types import FunctionType
list(FunctionType(f.__code__, globals())(1,2))
Exit_code=0

if __name__ == "__main__":
    import sys
    ret=main()
    sys.exit(exit_code)
