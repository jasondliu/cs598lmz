import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: wangsaichao
 * @date: 2018/5/24
 * @description: 商品分类
 */
@Data
@ApiModel(value = "商品分类")
public class ProductCategory implements Serializable {

    private static final long serialVersionUID = -83777161355605599L;

    @ApiModelProperty(value = "商品分类id")
    private Integer categoryId;

    @ApiModelProperty(value = "商品分类名称")
    private String categoryName;

    @ApiModelProperty(value = "商品分类编码")
    private String categoryCode;

    @ApiModelProperty(value = "商品分
