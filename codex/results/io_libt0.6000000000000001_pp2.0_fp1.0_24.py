import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author: liyong
 * @date: 2020/1/15
 * @description:
 */
@Data
@ApiModel(value = "登录信息")
public class LoginInfo {

    @ApiModelProperty(value = "用户名")
    private String username;

    @ApiModelProperty(value = "密码")
    private String password;
}
