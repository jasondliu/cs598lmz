import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.constraints.NotNull;

/**
 * @author: hxy
 * @description: 登录表单
 * @date: 2017/10/24 11:55
 */
@Data
@ApiModel(value = "登录表单")
public class LoginForm {
	@ApiModelProperty(value = "手机号")
	@NotNull(message = "手机号不能为空")
	private String mobile;

	@ApiModelProperty(value = "密码")
	@NotNull(message = "密码不能为空")
	private String password;

}
