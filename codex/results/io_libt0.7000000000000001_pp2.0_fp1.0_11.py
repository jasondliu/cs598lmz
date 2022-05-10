import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;

/**
 * @author yangjian
 * @since 2017-06-15 下午1:57.
 */
@RestController
@RequestMapping("/api/v2/user")
@Api(description = "用户管理")
public class UserControllerV2 {

	@Autowired
	private UserService userService;

	@ApiOperation(value = "分页查询用户列表", httpMethod = "GET")
	@ApiImplicitParams({
			@ApiImplicitParam(paramType = "header", name = "Authorization", value = "Bearer access_token", required =
