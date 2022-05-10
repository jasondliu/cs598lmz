import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.constraints.NotNull;

/**
 * @author: zhangcx
 * @date: 2019/10/21 10:44
 * @since:
 */
@Data
public class UserDTO {
    @ApiModelProperty(value = "用户名")
    @NotNull(message = "用户名不能为空")
    private String username;
    @ApiModelProperty(value = "密码")
    @NotNull(message = "密码不能为空")
    private String password;
}
