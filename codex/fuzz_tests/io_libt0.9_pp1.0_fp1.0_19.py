import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.Authorization;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;
import springfox.documentation.annotations.ApiIgnore;

/**
 * <p>
 * 文章收藏 前端控制器
 * </p>
 *
 * @author zwc
 * @since 2020-01-11
 */
@Api(value = "web服务", description = "文章收藏管理", tags = {"文章收藏管理"})
@RestController
@RequestMapping("/api/v1/article-collection")
public class ArticleCollectionController {

    private ArticleCollectionService articleCollectionService;

    public ArticleCollectionController(ArticleCollectionService articleCollectionService) {
        this.
