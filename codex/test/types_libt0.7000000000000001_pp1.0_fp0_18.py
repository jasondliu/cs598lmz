import types
types.SimpleNamespace

if 1:
    ################################################################################
    #
    # Example 1:
    #
    # Basic usage
    #
    ################################################################################

    # target_json is a JSON string to be parsed
    target_json = '{"key1" : "value1", "key2" : "value2"}'
    # target_json can be also a Python dictionary
    target_json = {"key1" : "value1", "key2" : "value2"}

    # parse target_json to namespace object
    parsed = JsonParser().parse(target_json)

    # access to parsed namespace object
    print("parsed.key1 = %s" % parsed.key1)
    print("parsed.key2 = %s" % parsed.key2)

    # parsed object is a namespace object and can be used as a dictionary
    print("parsed['key1'] = %s" % parsed['key1'])
    print("parsed['key2'] = %s" % parsed['key2'])

    # Type
