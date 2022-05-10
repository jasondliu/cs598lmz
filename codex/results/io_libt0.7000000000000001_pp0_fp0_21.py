import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.constraints.NotNull;
import java.util.List;

@Data
@ApiModel("插入通知请求参数")
public class NoticeInsertReq {

    @NotNull
    @ApiModelProperty("通知标题")
    private String title;

    @NotNull
    @ApiModelProperty("通知内容")
    private String content;

    @NotNull
    @ApiModelProperty("通知类型")
    private Integer type;

    @ApiModelProperty("通知接收者")
    private List<Long> receiver;
}
