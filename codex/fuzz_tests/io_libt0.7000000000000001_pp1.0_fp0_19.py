import io.swagger.annotations.Api;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;

@RestController
@Api(value = "用户管理", tags = "用户管理")
@RequestMapping(value = "/user", method = RequestMethod.POST)
public class UserController {

    @Autowired
    private UserService userService;


    @RequestMapping(value = "/register", method = RequestMethod.POST)
    public Result register(@RequestBody User user) {
        return userService.register(user);
    }

    @RequestMapping(value = "/login", method = RequestMethod.POST)
    public Result login(@RequestBody User user) {
        return userService.login(user);
    }

    @RequestMapping(value = "/updatePassword", method = RequestMethod.POST)
    public Result updatePassword(@
