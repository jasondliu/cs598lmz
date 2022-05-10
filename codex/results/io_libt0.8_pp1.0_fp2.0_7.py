import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.Enumeration;
import java.util.List;

/**
 * 设备状态控制器
 * @author 吴成卓
 * @version V1.0
 * @Project: fireControl_3D_web
 * @Package com.fireControl.main
 * @Description:
 * @date 2020/1/8 星期三 15:34
 */
@RestController
@RequestMapping("device")
@Api(value = "设备状态控制器")
public class DeviceStateController {
    @Autowired
    private DeviceStateService deviceStateService;
    @Autowired
    private DeviceModelService deviceModelService;
    @Autowired
   
