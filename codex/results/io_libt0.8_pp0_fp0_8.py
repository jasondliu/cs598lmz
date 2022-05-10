import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.List;

@ApiModel("分页实体")
@Data
public class PageDto<T> implements Serializable {

    private static final long serialVersionUID = -2212772543827896655L;

    @ApiModelProperty(value = "当前页", required = true)
    private Integer current;

    @ApiModelProperty(value = "每页条数", required = true)
    private Integer size;

    @ApiModelProperty(value = "总页数", required = true)
    private Integer pages;

    @ApiModelProperty(value = "总数", required = true)
    private Long total;

    @ApiModelProperty(value = "列表", required = true)
    private List<T> records;

    public Integer getCurrent() {
        return current;
    }


