import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.Valid;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.util.List;

/**
 * @author chentudong
 * @date 2020/3/21 14:57
 * @since 1.0
 */
@Data
@ApiModel(value = "添加角色参数")
public class RoleAddParam
{
    @ApiModelProperty(value = "角色名称", required = true)
    @NotBlank(message = "角色名称不能为空")
    private String name;

    @ApiModelProperty(value = "角色编码", required = true)
    @NotBlank(message = "角色编码不
