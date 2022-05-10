import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author Xiecai
 * @className UserDeleteDTO
 * @description TODO
 * @date 2020/6/8 9:14
 */
@Data
@ApiModel(value = "删除用户类")
public class UserDeleteDTO {

    @ApiModelProperty(value = "用户名")
    private String username;
}
