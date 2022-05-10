import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping(path = "/api/v1/roles", produces = MediaType.APPLICATION_JSON_VALUE)
@Api(tags = {"Roles"}, description = "Roles API")
public class RoleController {

    private final RoleService service;

    @Autowired
    public RoleController(RoleService service) {
        this.service = service;
    }

    @ApiOperation(value = "Find All Roles")
    @PreAuthorize("hasAuthority('ROLE_GET_ALL')")
    @GetMapping
    public List<Role> findAll() {
        return service.findAll();
    }

    @
