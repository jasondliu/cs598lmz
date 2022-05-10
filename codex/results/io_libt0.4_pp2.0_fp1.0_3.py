import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: yangyongkang
 * date:2020/4/13
 * time:17:37
 * description:
 **/
@Data
public class User implements Serializable {

	private static final long serialVersionUID = -8573034671567209838L;
	@ApiModelProperty(value = "用户id")
	private Long id;
	@ApiModelProperty(value = "用户名")
	private String username;
	@ApiModelProperty(value = "密码")
	private String password;
	@ApiModelProperty(value = "创建时间")
	private Date createTime;
	@ApiModelProperty(value = "更新时间")
	private Date updateTime;
	@ApiModelProperty(value = "状态")
	private
