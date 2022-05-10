import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;

/**
 * @author jiangyf
 * @date 2017/8/2
 */
@Data
@ApiModel("经销商分页查询条件")
public class DealerPageParam implements Serializable {
    private static final long serialVersionUID = -7717648099236412088L;

    @ApiModelProperty("经销商名称")
    private String dealerName;
    @ApiModelProperty("经销商编码")
    private String dealerCode;
    @ApiModelProperty("经销商类型")
    private Integer dealerType;
    @ApiModelProperty("省")
    private String province;
    @ApiModelProperty("市")
    private String
