import io.swagger.annotations.ApiModelProperty;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ApiModel(value = "根据用户ID查询发布的任务详情")
public class UserTaskBO2 {

    @ApiModelProperty(value = "任务ID")
    @JsonSerialize(using = ToStringSerializer.class)
    private Long taskId;

    @ApiModelProperty(value = "接包人姓名")
    private String realName;

    @ApiModelProperty(value = "接包人身份证")
    private String identityCard;

    @ApiModelProperty(value = "
