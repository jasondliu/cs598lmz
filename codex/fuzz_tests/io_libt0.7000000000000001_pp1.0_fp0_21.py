import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;

@Api(value = "用户相关操作",tags = "订单接口")
@RestController
@RequestMapping("/order")
@Slf4j
public class OrderController {
	
	@ApiOperation(value = "创建订单",notes = "创建订单")
	@RequestMapping(value = "/create", method = RequestMethod.POST)
	public Result<OrderInfo> create(@RequestBody OrderParam orderParam) {
		log.info("创建订单，入参为：{}",orderParam);
		OrderInfo orderInfo = new OrderInfo();
		BeanUtils.copyProperties(orderParam,orderInfo);
		return Result.success(orderInfo);
	}
	
	@ApiOperation(value = "修
