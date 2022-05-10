import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.experimental.Accessors;

import javax.validation.constraints.NotNull;

/**
 * @author zf
 */
@Data
@Accessors(chain = true)
public class EmployeeQueryDTO {

    @ApiModelProperty(value = "账号")
    private String account;

    @ApiModelProperty(value = "姓名")
    private String name;

    @ApiModelProperty(value = "部门id")
    private Integer deptId;

    @ApiModelProperty(value = "职务id")
    private Integer dutyId;

    @NotNull(message = "页码不能为空")
    @ApiModelProperty(value = "页码")
    private Integer pageNo;

    @NotNull(message = "每页数量不能为空")
    @
