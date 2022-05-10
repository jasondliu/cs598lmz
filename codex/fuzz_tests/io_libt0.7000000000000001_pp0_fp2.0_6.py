import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.io.Serializable;

/**
 * 用户信息
 */
@Data
@ApiModel(value = "用户信息")
public class UserInfo implements Serializable {

    @ApiModelProperty(name = "userId", value = "用户id", dataType = "Long", notes = "用户id")
    @NotNull(message = "用户id不能为空")
    private Long userId;

    @ApiModelProperty(name = "username", value = "用户名称", dataType = "String", notes = "用户名称")
    @NotBlank(message = "用户名称不能为空")
    private
