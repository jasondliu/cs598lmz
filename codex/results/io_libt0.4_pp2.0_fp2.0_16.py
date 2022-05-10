import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;

/**
 * @author: zhangcx
 * @date: 2019/9/25 15:22
 * @since:
 */
@Data
@ApiModel("角色列表")
public class RoleListVO {
    @ApiModelProperty("角色列表")
    private List<RoleVO> roleList;
}
