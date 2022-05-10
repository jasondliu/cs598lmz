import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import java.util.List;

/**
 * Created by dly on 2018/8/13.
 */
@ApiModel(value = "添加用户返回")
public class AddUserResponseDto extends  ResponseDto{

    @ApiModelProperty(value = "主键ID")
    private Integer id;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}
