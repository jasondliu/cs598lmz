import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @author: jia.xue
 * @create: 2019-08-26 16:04
 * @Description
 **/
@RestController
@RequestMapping(value = "/api/v1/user",produces = MediaType.APPLICATION_JSON_UTF8_VALUE)
@Api(description="用户管理")
public class UserController {

    @Autowired
    UserService userService;


    @ApiOperation(value = "用户
