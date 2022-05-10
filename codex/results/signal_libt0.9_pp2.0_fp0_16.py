import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

try:
    from secret import *
except:
    print "No 'SECRET.py' found, what's the TimeEntry client id you need to log in? (Press CTRL-C to abort)"
    cid = str(raw_input("> "))
    print "And the client secret?"
    csec = str(raw_input("> "))
    open("secret.py","w").write("CID={cid}; CSEC={csec}".format(cid=cid, csec=csec))
    from secret import *
assert len(CID) == 24, "Must be client_id of the form '12345678-abcd-1234-efgh-0123456789ab'."
assert len(CSEC) == 128, "Must be client_secret of the form '123456789abcdef123456789abcdef123456789abcdef123456789abcdef1234'."

default_access_token_filename = "access_token.json"

import
