import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Id;
import java.io.Serializable;
import java.util.Date;

/**
 * @program: tensquare_parent
 * @description: 实体类
 * @author: cf
 * @create: 2019-06-17 13:41
 */
@Entity
@Data
public class Column implements Serializable {
    @Id
    private String id;

    @ApiModelProperty(value = "专栏名称")
    private String name;

    @ApiModelProperty(value = "专栏简介")
    private String summary;

    @ApiModelProperty(value = "用户id")
    private String userid;

    @ApiModelProperty(value = "申请日期")
    private Date createtime;

    @ApiModelProperty(value = "审核日期
