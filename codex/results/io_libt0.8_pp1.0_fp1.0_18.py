import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;

@ApiModel("访问器模型")
@Data
public class AccessorVO {

    @ApiModelProperty("唯一标识")
    private String id;

    @ApiModelProperty("访问器名称")
    private String name;

    @ApiModelProperty("访问器显示名称")
    private String displayName;

    @ApiModelProperty("访问器描述")
    private String description;

    @ApiModelProperty("访问器所属空间")
    private String space;

    @ApiModelProperty("访问器所属空间展示名称")
    private String spaceDisplayName;

   
