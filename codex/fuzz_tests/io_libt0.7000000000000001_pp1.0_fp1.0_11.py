import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @author: zhangyy
 * @email: zhang10092009@hotmail.com
 * @date: 19-2-18 15:38
 * @version: 1.0
 * @description:
 */
@Slf4j
@RestController
@Api(value = "", tags = {"课程管理"})
@RequestMapping(value = "/course")
public class CourseController {

    private final CourseService courseService;

    @Autowired
    public CourseController(CourseService courseService) {
        this.courseService = courseService;
    }

    @ApiOperation(value = "保存课程信息")
    @PostMapping(value = "/save")
