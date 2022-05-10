import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import pers.zb.common.util.result.Result;
import pers.zb.entity.user.SysUser;
import pers.zb.pay.common.core.dwz.DWZ;
import pers.zb.pay.common.core.dwz.DwzAjax;
import pers.zb.pay.service.user.api.SysUserService;
import pers.zb.pay.service.user.exceptions.UserBizException;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/sys/user")
@Api(description="用户查询
