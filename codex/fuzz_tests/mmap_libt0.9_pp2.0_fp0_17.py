import mmap
import os

def print_usage():
    print "%s version %s" % (PROGRAM, VERSION)
    print ""
    print "usage: %s -h [<host> [<service_name>]]" % sys.argv[0]
    print ""
    print "Searches for, and reports on, TCP listener ports in a network"

def print_help():
    print_usage()
    print ""
    print "       -h            : Help."
    print ""
    print "       <host>        : Target host. (default: localhost)"
    print "       <service_name>: Port number or service name."
    print ""

def do_command(cmd):
    p = popen2.Popen4(cmd)

    stdo = ''
    while 1:
        stdo += p.fromchild.read()
        if stdo[-2:] == '\r\n':
            break

    return stdo[:len(stdo)-2]

def get_raw_service_by_name(service_name):
   
