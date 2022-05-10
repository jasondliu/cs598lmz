import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author: 八哥
 * @computer：Administrator
 * @create 2018-04-07 上午 10:02
 */
@RestController
@RequestMapping(value = "/user/")
@Api(description = "用户管理")
public class UserController {
    @Autowired
    private UserService userService;

    @ApiOperation(value = "分页查询所有用户信息", notes = "分页查询所有用户信息")
