import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;

/**
 * @author: zhangyh-k
 * @date: 2018/10/24
 * @description:
 */
@Data
public class UserInfo implements Serializable {
    @ApiModelProperty(value = "用户id")
    private Integer id;
    @ApiModelProperty(value = "用户名")
    private String username;
    @ApiModelProperty(value = "密码")
    private String password;
    @ApiModelProperty(value = "用户类型")
    private String userType;
    @ApiModelProperty(value = "用户状态")
    private String userStatus;
    @ApiModelProperty(value = "用户头像")
    private String userImg;
    @ApiModelProperty(value = "用户昵称")
    private String user
