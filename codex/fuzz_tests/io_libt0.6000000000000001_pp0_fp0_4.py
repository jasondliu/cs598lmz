import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import java.io.Serializable;
import java.util.List;

/**
 * @author: lzh
 * @date: 2019/9/6
 * @description:
 */
@Data
public class QueryUserRequestVO implements Serializable {
    private static final long serialVersionUID = -7074358015907879416L;

    @ApiModelProperty(value = "用户编码")
    private String userCode;

    @ApiModelProperty(value = "用户名称")
    private String userName;

    @ApiModelProperty(value = "角色Ids")
    private List<String> roleIds;

    @ApiModelProperty(value = "部门Ids")
    private List<String> departmentIds;

    @A
