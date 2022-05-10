import codecs
# Test codecs.register_error so that we dont die 
codecs._verbose = True
codecs._dotencode = codecs._dotencode_errors.get('error')
codecs._dotdecode = codecs._dotdecode_errors.get('error')
# End of Test codecs.register_error

# Test to see if we should get out of here.
if len(sys.argv) == 3 :
    templateName = sys.argv[2]
    if templateName == "getBaseTemp" :
        inputName = sys.argv[1]
        name = inputName.split('.')
        name = name[0]
        name = name.split('\\')
        name = name[-1]
        print name
        sys.exit(0)

# Do common setup
if len(sys.argv) == 2 :
    inputName = sys.argv[1]
    name = inputName.split('.')
    name = name[0]
    name = name.split('\\')
    name = name[-1]
    className =
