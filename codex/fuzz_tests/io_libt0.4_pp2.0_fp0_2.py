import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author zhangzhiqiang
 * @date 2019/6/29.
 * description：
 */
@Data
@ApiModel(value = "用户实体类")
public class User implements Serializable {
    private static final long serialVersionUID = -2713574518381269582L;
    @ApiModelProperty(value = "用户名")
    private String userName;
    @ApiModelProperty(value = "密码")
    private String password;
    @ApiModelProperty(value = "年龄")
    private Integer age;
    @ApiModelProperty(value = "生日")
    private Date birthday;
}
