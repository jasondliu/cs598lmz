import io.swagger.annotations.ApiModelProperty;

import java.util.Date;

/**
 * @author: zhangyh-k@glondon.com
 * @description:
 * @date: 2018/12/20
 * @time: 10:33
 */
@ApiModel(value = "客户管理")
public class Customer {
    @ApiModelProperty(value = "客户id")
    private Integer id;
    @ApiModelProperty(value = "客户名称")
    private String name;
    @ApiModelProperty(value = "客户手机号")
    private String mobile;
    @ApiModelProperty(value = "客户邮箱")
    private String email;
    @ApiModelProperty(value = "客户地址")
    private String address;
    @ApiModelProperty(value = "客户状态")
    private Integer status;
    @ApiModel
