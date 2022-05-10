import io.swagger.annotations.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * <p>
 *  前端控制器
 * </p>
 *
 * @author zx
 * @since 2018-08-06
 */
@Api(value = "账户信息接口")
@RestController
@RequestMapping("/account")
public class AccountController {
    private final AccountService accountService;
    private static Logger logger = LoggerFactory.getLogger(AccountController.class);
    public AccountController
