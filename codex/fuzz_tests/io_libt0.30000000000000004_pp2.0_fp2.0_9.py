import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;

/**
 * @author: zh
 * @date: 2020/4/1/001 13:55
 */
@Data
public class UserInfo implements Serializable {
    private static final long serialVersionUID = -7357733128905895485L;
    @ApiModelProperty(value = "用户id")
    private Long id;
    @ApiModelProperty(value = "用户名")
    private String username;
    @ApiModelProperty(value = "用户昵称")
    private String nickname;
    @ApiModelProperty(value = "用户头像")
    private String avatar;
    @ApiModelProperty(value = "用户手机号")
    private String mobile;
    @ApiModelProperty(value = "用户邮箱")
    private String email;
    @ApiModel
