import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;

/**
 * @author yan
 */
@Data
@ApiModel(value = "订单详情")
public class OrderDetail implements Serializable {
    @ApiModelProperty(value = "订单id")
    private Integer id;
    @ApiModelProperty(value = "订单编号")
    private String orderNo;
    @ApiModelProperty(value = "订单状态")
    private String orderStatus;
    @ApiModelProperty(value = "订单状态码")
    private Integer orderStatusCode;
    @ApiModelProperty(value = "订单类型")
    private String orderType;
    @ApiModelProperty(value = "订单类型码")
    private Integer orderTypeCode;
    @
