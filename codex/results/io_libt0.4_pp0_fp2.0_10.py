import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author: xieyj 
 * @since: 2016年7月27日 下午4:29:02 
 * @history:
 */
@Api(value = "api", description = "菜单接口")
@RestController
@RequestMapping(value = "/api/system/menu")
public class XN630020 extends BaseController {

    @Autowired
    private ISYSMenuAO sysMenuAO;

    @ApiOperation(value = "菜单列表", notes = "分页查询菜单列表")
    @RequestMapping(value = "/list", method = RequestMethod.GET)
    @ResponseBody
   
