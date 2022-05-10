import signal
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

if __name__ == '__main__':
    while True:
        try:
            con = ldap.initialize(LDAP_SERVER)
            con.simple_bind_s(LDAP_BIND_USER, LDAP_BIND_PASSWORD)
            print "OK"
        except ldap.INVALID_CREDENTIALS:
            print 'Your username or password is incorrect.'
            sys.exit()
        except ldap.LDAPError, e:
            if type(e.message) == dict:
                for (k, v) in e.message.iteritems():
                    print '%s: %s' % (k, v)
                print 'Error connecting to LDAP server. Check your configuration.'
                sys.exit()
            else:
                print e
                sys.exit()

        print "sleeping..."
        time.sleep(60)

    con.unbind_s()
