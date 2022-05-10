import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;

/**
 * @author zhouxin
 * @date 2018/11/23
 */
@Data
@ApiModel(value = "获取订单详情")
public class OrderDetailDTO {

    @ApiModelProperty(value = "订单id", required = true)
    private String orderId;

    @ApiModelProperty(value = "订单编号", required = true)
    private String orderNo;

    @ApiModelProperty(value = "订单状态", required = true)
    private Integer orderStatus;

    @ApiModelProperty(value = "订单状态描述", required = true)
    private String orderStatusDesc;

    @ApiModelProperty(value = "订单总金
