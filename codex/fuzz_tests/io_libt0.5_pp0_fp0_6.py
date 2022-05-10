import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author wangqiang26
 * @mail wangqiang26@jd.com
 * @Date 9:08 2018/11/15
 */
@Data
@ApiModel(value = "结算单商品信息")
public class SettlementGoodsInfo {

    @ApiModelProperty(value = "商品编码")
    private String skuId;

    @ApiModelProperty(value = "商品名称")
    private String skuName;

    @ApiModelProperty(value = "商品数量")
    private Integer skuNum;

    @ApiModelProperty(value = "商品单价")
    private BigDecimal skuPrice;

    @ApiModelProperty(value = "商品总价")
    private BigDecimal sku
