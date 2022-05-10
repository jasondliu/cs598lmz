import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;
import java.util.List;

@Data
@TableName("tb_goods")
public class Goods implements Serializable {
    @TableId(type = IdType.AUTO)
    @ApiModelProperty(value = "商品id",required = false)
    private Long id;
    @ApiModelProperty(value = "商品名称",required = true)
    private String name;
    @ApiModelProperty(value = "商品单价",required = true)
    private Long price;
    @ApiModelProperty(value = "商品图片",required = true)
    private String pic;
    @ApiModelProperty(value = "商品状态，1-正常，2-下架，3-
