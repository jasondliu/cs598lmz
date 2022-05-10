import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author: wangsaichao
 * @date: 2018/5/24
 * @description: 商品分类控制层
 */
@RestController
@RequestMapping("/category")
@Api(value = "商品分类接口")
public class CategoryController {

    @Autowired
    private CategoryService categoryService;

    /**
     * 根据父id查询子节点
     * @param parentId
     * @return
     */
    @GetMapping("/list")
    @ApiOperation(value = "查询商品分类",notes = "查询商品
