import select
# Test select.select is implemented on all platforms
s = select.select
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Test if SSL is available. Note, SSL must not be available when
# disable_ssl_certificate_validation execution parameter is set to true or
# when the request is made to plain HTTP servers
# ------------------------------------------------------------------------------
if __context__['execution_parameters'].get(SSLContext, None) is None:
    if __parameters__.get('disable_ssl_certificate_validation', False):
        LOG_STDOUT('PySys', 'WARNING: Running with SSL certificate validation disabled')
    else:
        LOG_STDOUT('PySys', 'WARNING: SSL is not available')


# ------------------------------------------------------------------------------
# Create a class to create SSLContext instances used while connecting to a
# HTTPS server
# ------------------------------------------------------------------------------
class SSLContextFactory:
    '''
    Request the SSL certificate validation policy and create a SSLContext instance
    '''

    def create_ssl_context(self):
        '''
        Create the SSLContext instance to be used for https connection.
        '''
        cert_validation_required = not __param
