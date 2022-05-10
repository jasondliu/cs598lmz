import socket
# Test socket.if_indextoname(0x13) == "eth0"


def gen_network_report(tracedata, ip_addr, fn_tmpl):
    """
    Generates the network report file, based on the template filename fn_tmpl
    It creates output file named "network-report-IPaddr.html"
    """
    klee_msg_off = tracedata.messages[0].offset

    net_mapping = tracedata.net_mappings
    net_tuple = [(net_mapping[i].offset, net_mapping[i].count, net_mapping[i].tid) for i in net_mapping]
    net_tuple.sort()

    template_env = Environment(
        autoescape=select_autoescape(['html', 'xml']),
        loader=FileSystemLoader(searchpath="."),
        trim_blocks=True,
        lstrip_blocks=True)

    template = template_env.get_template(fn_tmpl)

    report_filename = 'network-report-' + ip_addr + ".html"

