import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

/**
 * @Author: lingjun.jlj
 * @Date: 2020/5/13 11:18
 * @Description: 操作日志
 */
@Api(tags = "操作日志")
@RestController
@RequestMapping("/admin/operLog")
@Loader(true)
public 
