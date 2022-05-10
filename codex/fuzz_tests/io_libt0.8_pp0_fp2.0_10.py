import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * 角色控制器
 * @author zhangxiaoxin
 * @version 1.0
 * @date 2020/4/1 17:20
 */
@RestController
@RequestMapping("role")
@Api(value = "角色管理接口", description = "角色管理接口，提供角色的增、删、改、查")
@CrossOrigin
public class RoleController {

    @Autowired
    RoleService roleService;

    @ApiOperation(value = "获取所有角色",
