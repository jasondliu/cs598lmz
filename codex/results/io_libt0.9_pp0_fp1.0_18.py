import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

/**
 * 客户接口控制中心
 *
 * @author TongWei.Chen 2018-06-15 16:07:20
 */
@RestController
@Api(description = "客户接口管理")
public class CustomerAPI {
    @Resource
    private CustomerService customerService;

    @Resource
    private CustomerQueryService customerQueryService;


    @GetMapping("/customer/{id}")
    @ApiOperation(value = "按id查询")
    public R<CustomerVO> select(@PathVariable("id") Long id) {
        return R.ok(customerService.selectById(id));
    }

    @PostMapping("/customer")
    @ApiOperation(value = "新增")

