import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;

/**
 * @author: zhangyh-k@glondon.com
 * @description:
 * @date: 2018/12/25
 * @time: 14:31
 */
@Data
@ApiModel(value = "查询用户列表")
public class UserListQuery implements Serializable {

    @ApiModelProperty(value = "用户名")
    private String userName;

    @ApiModelProperty(value = "用户状态")
    private Integer userStatus;
}
