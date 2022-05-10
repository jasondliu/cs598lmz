import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: lujunwei
 * @time: 15:47 2019/1/10
 * @des:
 */
@Data
public class SysDict implements Serializable {
    @ApiModelProperty(value = "主键id", dataType = "Integer")
    private Integer id;

    @ApiModelProperty(value = "字典名称", dataType = "String")
    private String name;

    @ApiModelProperty(value = "字典类型", dataType = "String")
    private String type;

    @ApiModelProperty(value = "字典码", dataType = "String")
    private String code;

    @ApiModelProperty(value = "字典值", dataType = "String")
    private String value;

    @ApiModelProperty(value = "
