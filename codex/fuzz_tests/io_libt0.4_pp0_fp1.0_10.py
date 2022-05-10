import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

@Data
@ApiModel(value = "查询订单详情返回参数")
public class OrderDetailResponse {

    @ApiModelProperty(value = "订单号")
    private String orderId;

    @ApiModelProperty(value = "订单状态")
    private Integer orderStatus;

    @ApiModelProperty(value = "订单状态描述")
    private String orderStatusDesc;

    @ApiModelProperty(value = "订单总金额")
    private BigDecimal orderTotalPrice;

    @ApiModelProperty(value = "订单总数量")
    private Integer orderTotalNum;

    @ApiModelProperty(value = "订单支付方
