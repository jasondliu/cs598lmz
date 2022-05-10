import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author: hxy
 * @description: 登录表单
 * @date: 2017/10/24 11:53
 */
@Data
public class LoginForm {
	@ApiModelProperty(value = "账号")
	@NotBlank(message="账号不能为空")
	private String username;

	@ApiModelProperty(value = "密码")
	@NotBlank(message="密码不能为空")
	private String password;

	@ApiModelProperty(value = "验证码")
	@NotBlank(message="验证码不能为空")
	private String captcha;

	@ApiModelProperty(value = "uuid")
	@NotBlank(message="uuid不能为空")
	private String uuid;


