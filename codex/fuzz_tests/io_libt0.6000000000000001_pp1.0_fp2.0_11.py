import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpSession;

/**
 * @Author: zhouyongli
 * @Date: 2020/7/15 14:06
 * @create: 2020-07-15 14:06
 **/
@Controller
@Api(tags = "用户登录接口")
@RequestMapping("/user")
public class LoginController {
    @Autowired
    private UserService userService;

    @ApiOperation(value = "登录接口")
    @PostMapping("/login")
    @ResponseBody
    public ResponseData<User> login(@RequestParam("username") String username, @RequestParam("password") String password, HttpSession session) {
       
