import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.Authorization;
import io.swagger.annotations.AuthorizationScope;

@RestController
@RequestMapping("/api/v1/")
@Api(tags = "user")
public class UserController {
	@Autowired
	private UserService userService;

	@Autowired
	private JwtRequestFilter jwtRequestFilter;
	
	@Autowired
	private AuthenticationManager authenticationManager;

	@Autowired
	private JwtUtil jwtUtil;
	
	@PostMapping("/authenticate")
	@ApiOperation(value = "Authenticate the user", response = AuthenticationResponse.class)
	@ApiResponses(value = { @ApiResponse(code = 200, message = "Successful Login"),
			@ApiResponse(code =
