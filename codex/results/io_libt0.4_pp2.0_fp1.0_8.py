import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;

/**
 * @author: zhangyongkang
 * @date: 2020/1/15
 * @description:
 */
@Data
public class ListDTO<T> {

    @ApiModelProperty(value = "列表数据")
    private List<T> list;

    @ApiModelProperty(value = "总数")
    private Integer total;

    @ApiModelProperty(value = "当前页")
    private Integer page;

    @ApiModelProperty(value = "每页数量")
    private Integer size;
}
