import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;

@Data
@ApiModel(value = "菜单管理")
public class Menu {

    @ApiModelProperty(value = "菜单id", required = true)
    private String id;

    @ApiModelProperty(value = "菜单名称", required = true)
    private String name;

    @ApiModelProperty(value = "菜单编码", required = true)
    private String code;

    @ApiModelProperty(value = "菜单url", required = true)
    private String url;

    @ApiModelProperty(value = "菜单图标", required = true)
    private String icon;

    @ApiModelProperty(value = "菜单级别", required = true)
    private Integer level;

    @ApiModelProperty(value = "
