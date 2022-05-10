import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @Description:
 * @Author: yangtao
 * @CreateDate: 2019-05-31 19:37
 */
@RestController
@Api(tags = "商品评价管理")
@RequestMapping("/api/goodsComment")
public class GoodsCommentController {

    @Autowired
    private GoodsCommentService goodsCommentService;

    @PostMapping("/add")
    @ApiOperation("添加商品评价")
    public Result add(@RequestBody GoodsComment goodsComment) {
        goodsCommentService.add(goodsComment);
        return Result.success();
    }

    @PostMapping("/update")
    @ApiOperation("更新商品评价")

