import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @author : liuqitian
 * @date : 2018/7/4 10:18
 * @version : V1.2
 * 订单入口
 */
@Api(description = "订单API")
@RestController
@RequestMapping("/order")
public class OrderInfoController {

    @Autowired
    private IOrderInfoService orderInfoService;

    @ApiOperation("通过用户ID获取其所有订单")
