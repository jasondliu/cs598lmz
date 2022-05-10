import io.swagger.annotations.Api;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(tags = "单点登录接口")
@RestController
@RequestMapping("/sso_api")
public class SsoController {

    private SsoService ssoService;

    @Autowired
    public SsoController(SsoService ssoService) {
        this.ssoService = ssoService;
    }

    @PostMapping("/login")
    public ResponseEntity<CommonResult<TokenResult>> login(@RequestBody LoginVo loginVo){
        CommonResult<TokenResult> result = ssoService.login(loginVo
