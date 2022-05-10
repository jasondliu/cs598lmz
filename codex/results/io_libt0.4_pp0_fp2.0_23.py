import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;

import java.io.Serializable;
import java.math.BigDecimal;
import java.util.Date;

/**
 * <p>
 * 预付费账户表
 * </p>
 *
 * @author zy
 * @since 2019-11-22
 */
@Data
@EqualsAndHashCode(callSuper = false)
@TableName("t_prepaid_account")
@ApiModel(value="PrepaidAccount对象", description="预付费账户表")
public class PrepaidAccount implements Serializable {

    private static final long serialVersionUID = 1L;

    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    @ApiModelProperty(value = "用户ID")
    @TableField("user_id")
    private Integer userId;


