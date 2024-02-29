import sys
def printf(format,*args):
    sys.stdout.write(format.format(*args))
def scanf(format):
    return tuple(map(type(format),input().split()))
def puts(s):
    sys.stdout.write(s + "\n")
def gets():
    return sys.stdin.readline()
