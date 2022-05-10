import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@Api(tags = "消息推送")
@RestController
@Slf4j
@RequestMapping("/api/v1/message")
public class MessagePushController {

    @Resource
    private MessagePushService messagePushService;

    @ApiOperation(value = "发送消息", httpMethod = "POST")
   
