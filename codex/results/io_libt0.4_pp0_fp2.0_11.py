import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.io.Serializable;

/**
 * @author luojian
 * @date 2020/6/9
 */
@Data
public class AddRoleParam implements Serializable {
    private static final long serialVersionUID = -9178514553408192830L;

    @ApiModelProperty("角色名称")
    @NotBlank(message = "角色名称不能为空")
    private String name;

    @ApiModelProperty("角色描述")
    @NotBlank(message = "角色描述不能为空")
    private String description;

    @ApiModelProperty("角色状态")
   
