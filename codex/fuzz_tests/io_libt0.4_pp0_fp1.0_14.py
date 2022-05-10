import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.Date;

/**
 * @author luoyl
 * @create 2019/5/25 0025
 */
@Data
@ApiModel(value = "计划类型")
public class PlanTypeDto {
    @ApiModelProperty(value = "计划类型ID")
    private String id;
    @ApiModelProperty(value = "计划类型名称")
    private String name;
    @ApiModelProperty(value = "创建时间")
    private Date createTime;
    @ApiModelProperty(value = "创建人")
    private String createBy;
    @ApiModelProperty(value = "修改时间")
    private Date updateTime;
    @ApiModelProperty(value = "修改人")
    private String updateBy;
