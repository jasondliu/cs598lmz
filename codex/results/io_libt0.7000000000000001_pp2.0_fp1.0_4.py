import io.swagger.annotations.ApiModelProperty;
import java.io.Serializable;
import java.math.BigDecimal;
import java.util.Date;
import javax.persistence.*;

@Table(name = "sys_user_account")
@ApiModel(value="UserAccount对象", description="")
public class UserAccount implements Serializable {
    @Id
    @Column(name = "id")
    @ApiModelProperty(value = "主键id")
    private Integer id;

    @Column(name = "user_id")
    @ApiModelProperty(value = "用户id")
    private Integer userId;

    @Column(name = "balance")
    @ApiModelProperty(value = "用户余额")
    private BigDecimal balance;

    @Column(name = "create_time")
    @ApiModelProperty(value = "创建时间")
    private Date createTime;

    @Column(name = "update_time
