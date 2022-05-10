import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: hxy
 * @description: 登录日志
 * @date: 2017/10/24 11:53
 */
@Data
public class LoginLog implements Serializable {
	private static final long serialVersionUID = 1L;

	@ApiModelProperty(value = "id")
	private String id;

	@ApiModelProperty(value = "用户id")
	private String userId;

	@ApiModelProperty(value = "用户名")
	private String username;

	@ApiModelProperty(value = "登录时间")
	private Date loginTime;

	@ApiModelProperty(value = "登录ip")
	private String ip;

	@ApiModelProperty(value = "登录地点")
	private String location;

	@ApiModel
