import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.experimental.Accessors;

/**
 * @Description: 通用字典 头部返回
 * @Table: 通用字典
 * @Author: bell
 * @email:  bell@e-tonggroup.com
 * @Version: 1.0
 */
@Data
@EqualsAndHashCode(callSuper = false)
@Accessors(chain = true)
@ApiModel(value = "Dict对象", description = "通用字典 头部返回")
public class DictHeadDict implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "字典序号")
    private Integer id ;

    @ApiModelProperty(value = "字
