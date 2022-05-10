import io.swagger.annotations.ApiParam;
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * Created by lenovo on 2018/6/20.
 */
@RestController
@RequestMapping(value = "/api/admin/roles")
public class AdminRoleController extends BaseController{

    private static final Logger LOGGER = LoggerFactory.getLogger(AdminRoleController.class);

    @Autowired
    private RoleService roleService;

    @PostMapping(value = "")
    public Object create(
            @RequestParam(value = "name") String name,
            @RequestParam(value = "desc") String desc,
            @RequestParam(value = "idsStr") String idsStr,
            @RequestParam(value = "status") int status,
            @ApiParam(
