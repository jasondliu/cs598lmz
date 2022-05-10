import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/user")
@Api(value = "用户管理接口", description = "用户管理接口，提供用户的增、删、改、查")
public class UserController {

	@Autowired
	private UserService userService;

	@ApiOperation("查询所有用户信息")
	@GetMapping("/findAll")
	public List<User> findAll() {
		return userService.findAll();
	
