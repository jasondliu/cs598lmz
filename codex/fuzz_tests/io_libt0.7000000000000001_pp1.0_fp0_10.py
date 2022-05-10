import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/admin")
@Api(tags = "Admin")
public class AdminController {
    @Autowired
    private AdminService adminService;

    @ApiOperation(value = "Return List of all Users")
    @GetMapping("/users")
    public List<UserDto> getAllUsers() {
        return adminService.getAllUsers().stream().map(UserDto::new).collect(Collectors.toList());
    }

    @ApiOperation(value = "Return all roles")
    @
