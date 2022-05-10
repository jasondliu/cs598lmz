import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.Date;

/**
 * @author: zhangyy
 * @email: zhang10092009@hotmail.com
 * @date: 19-8-12 16:59
 * @version: 1.0
 * @description:
 */
@Data
@ApiModel(value = "学生课程订单")
public class StudentCourseOrderDto {
    @ApiModelProperty(name = "studentId", value = "学生id", dataType = "string")
    private String studentId;

    @ApiModelProperty(name = "classId", value = "班级id", dataType = "string")
    private String classId;

    @ApiModelProperty(name = "courseId", value = "课程id", dataType = "string")
    private String courseId;

    @ApiModelProperty(name = "courseName", value = "课程名称
