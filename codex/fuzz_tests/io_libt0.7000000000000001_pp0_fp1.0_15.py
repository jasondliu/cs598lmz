import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;


@RestController
@RequestMapping("/sys/user")
@Api(tags = "系统用户接口")
public class SysUserController {

    @Resource
    private SysUserService sysUserService;

    @PostMapping("/add")
    @ApiOperation(value = "新增用户接口", notes = "新增用户接口")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "id", value = "用户id", dataType = "String", paramType = "query"),
           
