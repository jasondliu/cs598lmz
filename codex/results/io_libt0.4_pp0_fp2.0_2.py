import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Api(value = "订单接口", description = "订单接口")
@RestController
@RequestMapping("/order")
public class OrderController {

    @Autowired
    private OrderService orderService;

    @ApiOperation(value = "获取订单列表", notes = "获取订单列表", httpMethod = "GET")
    @RequestMapping(value = "/getOrderList", method = RequestMethod.GET)
    public List<Order> getOrderList() {
        return orderService.getOrderList();
    }

    @ApiOperation(value = "获取订单详情", notes = "获取订单
