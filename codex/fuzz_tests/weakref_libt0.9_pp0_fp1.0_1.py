import weakref
import threading

from framework.common.frameworkcontroller import AMI_FWController

class AMI_DeviceManager(AMI_FWController):
    '''
        Controller of AMI device manager.
        Provide API for AMI User to control and manipulate the device.
    '''
    
    def __init__(self):
        '''
            Constructor
        '''
        AMI_FWController.__init__(self)

    def __del__(self):
        '''
            Destructor
        '''
        AMI_FWController.__del__(self)

    #===============================================================================
    #     Device Management API
    #===============================================================================
    @ami_logging(level='debug')
    def inject_device(self, device, nodeId=None):
        '''
            Inject a device on the network.

            @param device: the device library path.
            @param nodeId: the node id.
            @return: None
            @rtype: None
        '''
        try:
            self.get_internal_api('reserveFram
