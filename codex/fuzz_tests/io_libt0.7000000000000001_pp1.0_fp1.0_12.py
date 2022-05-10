import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import java.io.Serializable;
import java.util.List;

/**
 * @author 王亚楼(1374178468@qq.com)
 * @since 2019/9/26 10:17
 */
@ApiModel(description = "商品规格值")
public class SpecificationValueVo implements Serializable {
    private static final long serialVersionUID = 3639175548795753037L;

    @ApiModelProperty(value = "规格值名称")
    private String name;

    @ApiModelProperty(value = "规格值列表")
    private List<SpecificationDetailVo> details;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<SpecificationDetailVo
