import codecs
# Test codecs.register_error(JS.JS_Error)
def test_jar_helper():
    data = os.path.join(os.getenv("BROWSERCONTROL_HOME"), "browsertests/unittests.htm")
    try:
        codecs.register_error("javascript", JS.JS_Error)
        f = codecs.open(data, "rb", "latin-1", "replace", "javascript")
    finally:
        # Remove the error handler
        del codecs.lookup_error("javascript")
    f.close()

def test_browser_settings_options():
    broptions = BrowserSettingOptions()
    broptions.SetProxy("localhost:8080")
    broptions.SetProxyType("HTTP")
    broptions.AddAdditionalOption("key1","value11")
    broptions.AddAdditionalOption("key2","value22")
    # Add another one to test the unset.
    broptions.AddAdditionalOption("key1","value12")
    broptions.AddAdditionalOption("key1","value13")
    broptions.AddAdditionalOption("key
