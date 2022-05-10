import socket
socket.if_indextoname(int(args.interface))  # Check that interface exists

if args.verbose:
    print('Using interface: %s' % args.interface)
    print('Using network:   %s' % args.network)
    print('Using gateway:   %s' % args.gateway)

if args.dryrun:
    print('Dry-run mode enabled!')

subprocess.call(['ip', 'link', 'set', 'dev', args.interface, 'down'])
subprocess.call(['ip', 'addr', 'flush', 'dev', args.interface])
subprocess.call(['ip', 'route', 'flush', 'dev', args.interface])

subprocess.call(['ip', 'link', 'set', 'dev', args.interface, 'up'])
subprocess.call(['ip', 'route', 'add', 'default', 'via', args.gateway])
subprocess.call(['ip', 'addr', 'add', args.network, 'dev', args.interface])

if args.dryrun:
    print('Dry-run mode
