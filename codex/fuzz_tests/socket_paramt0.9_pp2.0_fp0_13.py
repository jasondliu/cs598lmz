import socket
socket.if_indextoname(interface)
opts.iface = re.sub('[0-9]+: ', '', opts.iface)
dev = opts.iface


def restore_tc_config(backupfile):
    with open(backupfile, 'rb') as fh:
        tcset = yaml.load(fh)

    if not isinstance(tcset, dict):
        return
    if not tcset.get('version', None):
        return

    def create_qdisc(q, dev):
        shell('ip link set dev {dev} qlen {qlen}')
        q = q.strip().split(' ')
        cmd = ('tc qdisc add dev {dev} {handle} ' +
               '{parent} {type}').format(dev=dev,
                                         handle=q[0],
                                         parent=q[1],
                                         type=q[2]
                                         )
        if q[2] == 'pie':    # pie has more parameters
            cmd += ' tupdate {tupdate} target {target} alpha {alpha} beta {beta
