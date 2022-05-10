import io.swagger.annotations.ApiModelProperty;
import java.io.Serializable;
import java.math.BigDecimal;
import java.util.Date;
import lombok.Data;

/**
 * 订单退货申请
 * 
 * @author zhulei
 * @email sunlightcs@gmail.com
 * @date 2020-08-06 17:20:12
 */
@ApiModel
@Data
@TableName("oms_order_return_apply")
public class OrderReturnApplyEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	/**
	 * $column.comments
	 */
	@TableId
	@ApiModelProperty(name = "id",value = "$column.comments")
	private Long id;
	/**
	 * $column.comments
	 */
	@ApiModelProperty(name = "orderId",value = "$column.comments")
	private Long orderId;
	/**
	 * $column.comments
	 */
	@ApiModelProperty(name
