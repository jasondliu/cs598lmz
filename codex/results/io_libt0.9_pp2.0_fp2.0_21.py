import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@CrossOrigin(origins = "http://localhost:4200")
@Api(description = "userApi")
@RestController
public class UserController {

    @Autowired
    private UserService userService;


    @RequestMapping(value = "auth/sign-up", method = RequestMethod.POST)
    @ApiOperation(value = "sign up")
    public ResponseData signUp(@RequestBody UserSignUpDTO userSignUpDTO) {
        try {
            if (userSignUpDTO.getPassword().equals(userSignUpDTO.getPassword())) {
                User user = new User(userSignUpDTO);
                user.setRole(Role.ADMINISTRATOR);
                userService.create(user);
                return new ResponseData(HttpStatus.OK.getReasonPh
