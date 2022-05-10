import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author: wangsaichao
 * @date: 2018/4/26
 * @description: 用户控制器
 */
@RestController
@RequestMapping(value = "/user")
@Api(value = "用户相关接口",description = "用户相关接口")
public class UserController {

    @Autowired
    private UserService userService;

    /**
     * 获取用户信息
     * @param id
     * @return
     */
    @ApiOperation(value = "获取用
