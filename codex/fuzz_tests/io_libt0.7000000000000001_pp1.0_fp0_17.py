import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: lirb
 * @date: 2019/5/14
 * @description:
 */
@Data
public class ReqUser implements Serializable {

    private static final long serialVersionUID = -1L;
    /**
     * 用户唯一id
     */
    @ApiModelProperty(value = "用户唯一id", required = true)
    private String id;
    /**
     * 姓名
     */
    @ApiModelProperty(value = "姓名")
    private String name;
    /**
     * 性别，0女，1男
     */
    @ApiModelProperty(value = "性别，0女，1男")
    private Integer sex;
    /**
     * 生日
     */
    @A
