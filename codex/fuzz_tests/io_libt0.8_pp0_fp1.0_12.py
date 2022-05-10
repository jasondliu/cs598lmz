import io.swagger.annotations.ApiModelProperty;
import org.hibernate.validator.constraints.NotBlank;

/**
 * @author lengleng
 * @date 2018/1/20
 * 邮件配置类，数据存覆盖式存入数据存
 */
@ApiModel(description = "邮件配置类")
public class EmailConfig {
    @ApiModelProperty(value = "邮件服务器SMTP地址")
    @NotBlank
    private String host;

    @ApiModelProperty(value = "邮件服务器 SMTP 端口")
    @NotBlank
    private String port;

    @ApiModelProperty(value = "发件者用户名")
    @NotBlank
    private String user;

    @ApiModelProperty(
