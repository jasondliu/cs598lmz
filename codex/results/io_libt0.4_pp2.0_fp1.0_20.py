import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.List;

/**
 * @author zhangxin
 * @date 2019/12/11
 */
@Data
@ApiModel(value = "角色列表")
public class RoleListVO implements Serializable {
    private static final long serialVersionUID = -1754277660149571801L;

    @ApiModelProperty(value = "角色列表")
    private List<RoleVO> roleVOList;

    @ApiModelProperty(value = "角色总数")
    private Integer total;
}
