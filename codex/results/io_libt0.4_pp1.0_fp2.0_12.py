import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;

/**
 * @author liuxiaokun
 * @version 1.0.0
 * @date 2020/9/11 16:20
 */
@Data
@ApiModel(value = "查询订单列表返回参数")
public class OrderListResponse extends BaseResponse {

    @ApiModelProperty(value = "订单列表")
    private List<OrderListDTO> orderList;
}
