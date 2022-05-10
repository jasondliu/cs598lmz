import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

/**
 * 
 * @author zhangpeng
 * @date 2017-04-01
 *
 */
@ApiModel
public class SysUserRoleDto implements Serializable {

	private static final long serialVersionUID = -7923342660446444103L;
	@ApiModelProperty(value = "用户id")
	private String userId;
	@ApiModelProperty(value = "角色id")
	private String roleId;
	public String getUserId() {
		return userId;
	}
	public void setUserId(String userId) {
		this.userId = userId;
	}
	public String getRoleId() {
		return roleId;
	}
	public void setRoleId(String roleId) {
		this.roleId = roleId;
	}
	
}
