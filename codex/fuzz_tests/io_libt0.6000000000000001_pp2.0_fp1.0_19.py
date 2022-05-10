import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.Date;

/**
 * 标签
 *
 * @author xiaojf 2017/11/18 10:25
 */
@ApiModel
@Data
public class TagVO {
    @ApiModelProperty(value = "标签id")
    private Integer id;
    @ApiModelProperty(value = "标签名称")
    private String name;
    @ApiModelProperty(value = "状态(0:未启用,1:启用)")
    private Integer status;
    @ApiModelProperty(value = "标签类型(0:自定义标签,1:系统标签)")
    private Integer type;
    @ApiModelProperty(value = "创建
