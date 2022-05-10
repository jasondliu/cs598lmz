import _struct
import com.cloudipc.surface.adapter
import com.cloudipc.utils.TCarListHelper
import com.cloudipc.utils.TErrNum
import com.cloudipc.utils.TVehicleInfo
import com.cloudipc.utils.TVehicleInfoListHelper
import com.cloudipc.vec.api
import com.cloudipc.vec.media
import com.cloudipc.vec.utils
import android.os.SystemClock
import android.util.Log
import com.cloudipc.RTCMmanager
import android.view.IWindowManager
import com.cloudipc.utils.TRect

py_module = None

def init(mod):
    global py_module
    logging.info('init')
    py_module = mod
    
class DevState():
    
    def __init__(self):
        self.run = 0 # 状态
        self.err = 0
        
    def isRunning(self):
        return self.run == 1
    
    def setErr(self,id):
