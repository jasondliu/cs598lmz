import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.constraints.NotNull;

/**
 * @author: wangsaichao
 * @date: 2018/5/14
 * @description: 删除角色请求参数
 */
@Data
@ApiModel(value = "删除角色请求参数")
public class RoleDeleteRequest {

    /**
     * 角色id
     */
    @NotNull(message = "角色id不能为空")
    @ApiModelProperty(value = "角色id",required = true)
    private Integer roleId;
}
