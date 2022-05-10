import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * @author jiumin
 * @create 2018-09-27 下午3:03
 **/
@Api()
@RestController
public class DemoController {

    private Logger logger = LoggerFactory.getLogger(this.getClass());

    @Autowired
    private DemoService demoService;

    @GetMapping("/hello")
    @ApiOperation(value="hello接口", notes="测试接口")
    public String hello() {
        logger.info("call hello");
        return "hello world";
    }

    @PostMapping("/say_hello")
    public String sayHello(@RequestParam("name") String name) {
        logger.info("call say_hello");
       
