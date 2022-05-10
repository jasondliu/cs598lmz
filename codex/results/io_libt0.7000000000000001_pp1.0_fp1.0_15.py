import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;

@RestController
@RequestMapping("/user")
@Api(value = "用户API", description = "用户API")
@Validated
public class UserController {

    @Autowired
    private UserService userService;

    @ApiOperation(value = "用户查询", notes = "用户查询")
    @ApiImplicitParam(paramType = "query", name = "user
