import codecs
codecs.register_error("escapereplace", escapereplace)


# Allow setting IP address:port (as an xoption)
# In particular, use port 0 to randomize a port that can be used with tshark(1) -port
class MyXoptionParser(optparse.OptionParser):
    def check_values(self, values, args):
        options = super(MyXoptionParser, self).check_values(values, args)
        if options.bind_addr:
            try:
                ip, port = options.bind_addr.split(':')
                options.bind_ip, options.bind_port = ip, int(port)
            except Exception:
                self.error("Bind Args (-b) should be of form IP[:port]")
            del options.bind_addr
        return options

def parse_args(command_line_args, ws_proto_options, ws_server_options):

  parser = MyXoptionParser(add_help_option=False)

  parser.add_option("--help", action="callback",
    callback=lambda o, p, e, d=
