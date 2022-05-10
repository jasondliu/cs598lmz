import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@Api(tags = {"计划"})
@RequestMapping("/plan")
public class PlanController {
    @Autowired
    private PlanService planService;

    @ApiOperation(value = "查找所有计划")
    @GetMapping
    public List<Plan> findAllPlan() {
        return planService.findAllPlan();
    }

    @ApiOperation(value = "查找指定计划")
    @GetMapping("/{id}")
    public Plan findPlanById(@PathVariable @ApiParam(value = "计划ID", required = true) Integer
