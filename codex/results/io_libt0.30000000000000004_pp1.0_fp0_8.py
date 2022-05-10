import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.Date;

/**
 * @author: wangsaichao
 * @date: 2018/5/25
 * @description: 商品分类
 */
@Data
public class ProductCategory {

    /**
     * 分类id
     */
    @ApiModelProperty(value = "分类id")
    private Integer categoryId;

    /**
     * 分类名称
     */
    @ApiModelProperty(value = "分类名称")
    private String categoryName;

    /**
     * 分类编号
     */
    @ApiModelProperty(value = "分类编号")
    private Integer categoryType;

    /**
     * 创建时间
     */
    @ApiModelProperty(value = "创建时
