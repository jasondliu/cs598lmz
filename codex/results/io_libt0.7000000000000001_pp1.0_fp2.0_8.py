import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.stream.annotation.EnableBinding;
import org.springframework.integration.support.MessageBuilder;
import org.springframework.messaging.MessageChannel;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(tags = "MQ")
@RestController
@RequestMapping("/rabbit")
//@EnableBinding(Source.class)
public class SendMessageController {
    /**
     * 消息发送管道
     */
//    @Autowired
//    private MessageChannel output;
    @ApiOperation(value = "向MQ发送消息", notes = "向MQ发送消息")
    @
