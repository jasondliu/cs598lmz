import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.experimental.Accessors;

import java.io.Serializable;

/**
 * @author: wangsaichao
 * @date: 2018/5/30
 * @description: 分页查询基类
 */
@Data
@Accessors(chain = true)
public class BaseQuery implements Serializable {

    private static final long serialVersionUID = -8696775543636182426L;

    @ApiModelProperty(value = "页码")
    private Integer pageNum = 1;

    @ApiModelProperty(value = "每页显示数量")
    private Integer pageSize = 10;
}
