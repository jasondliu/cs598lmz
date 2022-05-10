import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Random;

/**
 * @author JachinLin
 * @date 2019/9/9 - 9:56
 */
@RestController
@Api(tags = "测试Redis中的业务")
@RequestMapping("mq")
public class TestController {
    @Autowired
    StringRedisTemplate redisTemplate;
    @Autowired
