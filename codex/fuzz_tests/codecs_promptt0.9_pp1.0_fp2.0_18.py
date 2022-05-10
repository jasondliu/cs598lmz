import codecs
# Test codecs.register_error('logger', LoggerErrorHandler())
codecErrorHandlerFactory = codecs.CodecInfo(
    name='logger',
    encode=LoggerErrorHandler().encode,
    decode=LoggerErrorHandler().decode,
)
register_error('logger', codecErrorHandlerFactory)
encoded = encodeLogger(u"""When you make a typo in a Slack message, a red squiggle appears underneath the word to indicate a problem. Is there some such standard way to indicate a problem with a code sample in a blog post?""")

# Test codecs.register_error('surrogateescape', SurrogateEscapeErrorHandler())
codecErrorHandlerFactory = codecs.CodecInfo(
    name='surrogateescape',
    encode=SurrogateEscapeErrorHandler().encode,
    decode=SurrogateEscapeErrorHandler().decode,
)
register_error('surrogateescape', codecErrorHandlerFactory)
encoded = encodeSurrogateEscape(u"""When you make a typo in a Slack message, a red squiggle appears underneath the word to indicate a problem. Is there
