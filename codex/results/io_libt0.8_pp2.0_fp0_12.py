import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;

/**
 * 系统抽奖结果DTO
 *
 * @author chenzhenjia
 * @since 2020-03-23
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@ApiModel(value="SysLotteryResultDTO对象", description="系统抽奖结果")
public class SysLotteryResultDTO implements Serializable {

    private static final long serialVersionUID=1L;

    @ApiModelProperty(value = "系统抽奖结果ID")
    @JsonSerialize(using = ToStringSerializer.class)
    private Long id;

    @ApiModelProperty(value = "用户ID")

