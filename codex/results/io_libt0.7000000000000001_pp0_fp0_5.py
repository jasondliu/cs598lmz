import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

@Data
@ApiModel(value="阳光信用检索", description="阳光信用检索")
public class QueryCaseSunshine extends PageInfo {

    @ApiModelProperty(value = "案件id", example = "")
    private String caseId;

    @ApiModelProperty(value = "案件编号", example = "")
    private String caseNo;

    @ApiModelProperty(value = "案件状态", example = "")
    private String caseStatus;

    @ApiModelProperty(value = "通讯地址", example = "")
    private String address;

    @ApiModelProperty(value = "案件开始日期", example = "")
    private String caseStartDate;

    @ApiModelProperty(value = "案件
