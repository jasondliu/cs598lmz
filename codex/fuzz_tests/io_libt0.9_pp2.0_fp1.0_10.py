import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author haifeng
 * @date 2020-06-09 18:04
 */
@RestController
@RequestMapping("api/articleTag")
@Api(value = "ArticleTag", tags = "文章标签")
public class ArticleTagController {

    @Autowired
    private ArticleTagService articleTagService;

    @GetMapping("listTag")
    @ApiOperation(value = "获取文章标签", notes = "获取文章标签")
    public Result listTag() {
        return ResultUtil.success(articleTagService
