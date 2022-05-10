import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;

/**
 * @author zhangzhiqiang
 * @date 2019/7/8.
 * description：
 */
@Data
@ApiModel("分页返回结果")
public class PageResult<T> {
    @ApiModelProperty("总记录数")
    private Long total;
    @ApiModelProperty("分页数据")
    private List<T> rows;
}
