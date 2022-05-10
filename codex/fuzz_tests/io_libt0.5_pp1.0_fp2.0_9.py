import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author: yangchun
 * @description:
 * @date: Created in 2020-06-12 16:24
 */
@Api(tags = "系统菜单")
@RestController
@RequestMapping("/menu")
public class MenuController {

    @Autowired
    private MenuService menuService;

    @ApiOperation("获取所有菜单")
    @GetMapping
    public Result<List<Menu>> getAllMenu(){
        List<Menu> menuList = menuService.getAllMenu();
        return new Result<>(menuList);
    }

    @ApiOperation("获取角色所有菜单")
    @
