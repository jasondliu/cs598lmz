import codecs
codecs.register_error('ignore', codecs.replace_errors)

# Set up logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

# Define the module's virtual name
__virtualname__ = 'openstack'

# Functions
def __virtual__():
    '''
    Only load this module if the openstack module is available in __salt__
    '''
    return __virtualname__ if 'openstack.configured' in __salt__ else False


def _get_conn(conn_type='compute'):
    '''
    Return a conn object for the passed VM data
    '''
    if 'config.option' in __salt__:
        cloud_config = __salt__['config.option']('openstack')
    else:
        cloud_config = __opts__.get('openstack', {})

    if conn_type == 'compute':
        return novaclient.client.Client(
            cloud_config['config']['config_compute']['auth_version'],
           
