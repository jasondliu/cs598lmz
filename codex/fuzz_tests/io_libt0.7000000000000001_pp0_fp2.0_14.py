import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;

@RestController
@RequestMapping("/api/v1/log")
@Api(tags = "日志管理")
public class LogController {

	@Autowired
	private ILogService logService;

	@GetMapping("/login")
	@ApiOperation(value = "登录日志")
	@ApiImplicitParams({
			@ApiImplicitParam(name = "page", value = "页码", dataType = "int", paramType = "query", required = false),
			@ApiImplicitParam(name = "pageSize", value = "页大小", dataType = "int", paramType = "query", required = false),
			@ApiImplicitParam(name = "start
