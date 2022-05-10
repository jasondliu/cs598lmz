import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

@Api(value = "部门管理接口",description = "部门管理接口，提供部门的增、删、改、查")
@RestController
@RequestMapping("/department")
@CrossOrigin
public class DepartmentController {

    @Autowired
    private DepartmentService departmentService;

    @Autowired
    private JwtUtil jwtUtil;

    @ApiOperation("查询所有部门")
    @RequestMapping(method = RequestMethod.GET)
    public Result findAll(){
       
