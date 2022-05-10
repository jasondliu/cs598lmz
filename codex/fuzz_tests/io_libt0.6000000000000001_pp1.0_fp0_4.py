import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("/api/v1/users")
@Slf4j
public class UserController {

    @Autowired
    UserService userService;

    @ApiOperation(value = "Create a user")
    @PostMapping
    public UserDTO create(@RequestBody @Valid UserDTO userDTO) {
        log.info("Creating user {}", userDTO);
        return userService.create(userDTO);
    }

    @ApiOperation(value = "Get a user by id")
    @GetMapping("/{id}")
    public UserDTO getById(@ApiParam(value
