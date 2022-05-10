import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author: liu.tao
 * @create: 2020-09-14 13:21
 * @version: 1.0
 */
@Data
@ApiModel(value = "登录请求参数")
public class LoginReq {
    @ApiModelProperty(value = "用户名", required = true)
    private String username;
    @ApiModelProperty(value = "密码", required = true)
    private String password;
    @ApiModelProperty(value = "验证码", required = true)
    private String code;
}
