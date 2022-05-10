import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * 实体类
 *
 * @author makejava
 * @since 2020-05-15 17:51:03
 */
@Data
@ApiModel(value = "对象", description = "")
public class TbSku implements Serializable {
    private static final long serialVersionUID = -14088435632326863L;

    @TableId(value = "id", type = IdType.AUTO)
    @ApiModelProperty(value = "", name = "id", required = true, dataType = "Long")
    private Long id;

    @ApiModelProperty(value = "商品id", name = "spuId", required = true, dataType = "Long")
    private Long spuId;

    @ApiModelProperty(value = "商品标题", name = "title", required
