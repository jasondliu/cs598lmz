import sys, threading
threading.Thread(target=lambda: sys.stdout.write('abc')).start()

print("abc", file=sys.stdout)

## r1

print("ab\n" * 3)

## r2

import sys, threading
threading.Thread(target=lambda: sys.stdout.write("ab\n")).start()

print("ab\n", file=sys.stdout)

## r3

import sys
sys.stdout.write("\a")

## r4

print("\a")

## r5

import sys
sys.stdout.write("abc\fdef\n")

## r6

import sys
sys.stdout.write("abc\tdef\n")

## r9

print("abc\fdef")

## r10

print("abc\tdef")


## s1

print("\033[K")

## s2

print("\r\033[K", file=sys.stdout)

## s3

print("\r\033[K", end='
