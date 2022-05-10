import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.Date;

/**
 * @author wyw
 * @version 1.0
 * @date 2020/2/16 14:43
 */
@Data
@ApiModel(value = "测试用户实体类")
public class User {

    @ApiModelProperty(value = "用户id",required = true)
    private Long id;
    @ApiModelProperty(value = "用户名",required = true)
    private String username;
    @ApiModelProperty(value = "密码",required = true)
    private String password;
    @ApiModelProperty(value = "电话",required = true)
    private String phone;
    @ApiModelProperty(value = "地址",required = true)
    private String address;
    @ApiModelProperty(value = "创
