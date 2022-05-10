import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author: hxy
 * @description: 登录表单
 * @date: 2017/10/24 11:53
 */
@Data
public class LoginForm {
	@ApiModelProperty(value = "用户名", required = true)
	@NotBlank(message = "用户名不能为空")
	private String username;

	@ApiModelProperty(value = "密码", required = true)
	@NotBlank(message = "密码不能为空")
	private String password;

	@ApiModelProperty(value = "唯一标识", required = true)
	@NotBlank(message = "唯一标识不能为空")
	private String uuid = "";
}
