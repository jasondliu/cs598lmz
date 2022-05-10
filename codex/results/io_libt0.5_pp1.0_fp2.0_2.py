import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/user")
@CrossOrigin
@Api(value = "用户接口",description = "用户接口")
public class UserController {

    @Autowired
    private UserService userService;

    @ApiOperation(value = "获取用户列表",notes = "获取用户列表")
    @RequestMapping(value = "/getUserList",method = RequestMethod.GET)
    public List<User> getUserList(){
        return userService
