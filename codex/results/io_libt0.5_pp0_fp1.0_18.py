import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.List;

/**
 * @author ：xujin
 * @date ：Created in 2019/4/17 16:07
 * @description：
 */
@Data
@ApiModel(value = "分页查询用户信息")
public class QueryUserInfoPageResponse implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "总记录数")
    private long total;

    @ApiModelProperty(value = "总页数")
    private long pages;

    @ApiModelProperty(value = "当前页")
    private long pageNum;

    @ApiModelProperty(value = "每页显示数")
    private long
