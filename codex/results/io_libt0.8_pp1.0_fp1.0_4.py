import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @author cj
 * @date 2019/11/13
 */
@Api(value = "角色控制器",tags = "角色控制器")
@RestController
@RequestMapping("/role")
public class RoleController {

    @Autowired
    private RoleService roleService;


    @ApiOperation("查询所有可用角色")
    @GetMapping("/findAllAvailableRole")
    @PreAuthorize("hasRole('
