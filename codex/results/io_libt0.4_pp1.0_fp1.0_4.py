import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: zhangyy
 * @email: zhang10092009@hotmail.com
 * @date: 19-5-23 14:47
 * @version: 1.0
 * @description:
 */
@Data
@ApiModel(value = "学生作业答题信息")
public class StudentWorkAnswerDto implements Serializable {
    @ApiModelProperty(name = "answerId", value = "答题id", dataType = "string")
    private String answerId;
    @ApiModelProperty(name = "workId", value = "作业id", dataType = "string")
    private String workId;
    @ApiModelProperty(name = "studentId", value = "学生id", dataType = "string")
    private String studentId;

