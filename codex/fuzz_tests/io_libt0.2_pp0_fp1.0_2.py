import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: wangsaichao
 * @date: 2018/5/7
 * @description: 商品分类
 */
@Data
public class ProductCategory implements Serializable {

    private static final long serialVersionUID = -8297927802318490095L;

    @ApiModelProperty(value = "商品分类id")
    private Integer id;

    @ApiModelProperty(value = "分类名称")
    private String name;

    @ApiModelProperty(value = "分类编码")
    private String code;

    @ApiModelProperty(value = "分类父级id")
    private Integer parentId;

    @ApiModelProperty(value = "分类级别")

