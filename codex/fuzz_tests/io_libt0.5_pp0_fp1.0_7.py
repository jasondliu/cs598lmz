import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.List;

/**
 * @author luoyong
 * @Description: SysRoleController
 * @create 2019-12-10 22:21
 * @last modify by [LuoYong 2019-12-10 22:21]
 **/
@Api(tags = "角色管理")
@RestController
@RequestMapping("/sys/role")
@Slf4j
public class SysRoleController extends BaseController {

    @Resource
    private SysRoleService sysRoleService;

    @PostMapping("/add")
    @ApiOperation(value = "添加角色", notes = "
