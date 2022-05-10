import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.List;

/**
 * @游魁
 * @date 2018/11/8-10:46
 */
@Api(value = "首页", description = "首页")
@RestController
@RequestMapping("/api/home")
public class HomeInfoController extends BaseController {

    @Autowired
    private HomeInfoService homeInfoService;
    @Autowired
    private UserLoginService userLoginService;

    /**
     * 获
