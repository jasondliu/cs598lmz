import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

/**
 * ClassName: Address
 * Description:
 * date: 2020/1/9 9:33
 *
 * @author 小狐
 * @since JDK 1.8
 */
@ApiModel(value = "地址")
public class Address {
    @ApiModelProperty(value = "地址id")
    private Integer id;
    @ApiModelProperty(value = "地址详情")
    private String addressDetail;
    @ApiModelProperty(value = "地址类型")
    private Integer type;
    @ApiModelProperty(value = "省")
    private String province;
    @ApiModelProperty(value = "市")
    private String city;
    @ApiModelProperty(value = "区")
    private String area;
    @ApiModelProperty(value = "用户id")
    private
