import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;

@Data
@ApiModel(value = "基础实体类")
public class BaseEntity implements Serializable {
    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "创建时间")
    private String createdTime;

    @ApiModelProperty(value = "修改时间")
    private String updatedTime;

    @ApiModelProperty(value = "是否删除")
    private Boolean isDeleted;
}
