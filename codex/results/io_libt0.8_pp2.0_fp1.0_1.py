import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

@Data
@ApiModel
public class FeedbackDetailDTO implements Serializable {

    private static final long serialVersionUID = -7568767045262033394L;

    @ApiModelProperty(value = "问题类型", required = true)
    private String problemType;

    @ApiModelProperty(value = "文件列表", required = true)
    private String fileList;

    @ApiModelProperty(value = "反馈内容", required = true)
    private String content;

    @ApiModelProperty(value = "姓名", required = true)
    private String realName;

    @ApiModelProperty(value = "联系电话", required = true)
    private String phoneNumber;

    @ApiModelProperty(value = "处理状态", required
