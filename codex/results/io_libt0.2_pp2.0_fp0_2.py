import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;

/**
 * @author: zhangyh-k@glondon.com
 * @description:
 * @date: 2018/12/26
 * @time: 16:15
 */
@Data
@ApiModel(value = "用户信息")
public class UserInfo implements Serializable {
    private static final long serialVersionUID = -8170981276007049087L;
    @ApiModelProperty(value = "用户id")
    private Long id;
    @ApiModelProperty(value = "用户名")
    private String username;
    @ApiModelProperty(value = "用户昵称")
    private String nickname;
    @ApiModelProperty(value = "用户头像")
    private String avatar;
    @ApiModelProperty(value = "
