import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

/**
 * @Author: liujinhui
 * @Date: 2019/11/21 0:19
 */
@Controller
@RequestMapping("/app/user")
public class UserController {

    /**
     * 依赖注入
     */
    @Autowired
    private UserService userService;


    @GetMapping("/list")
    @ResponseBody
    public ResponseEntity<List<User>> queryAll() {
        List<User> list = userService.queryAll();
        return ResponseEntity.ok(list);
    }

    /**
     * 使用swagger2 生成api
     * @param start
     * @
