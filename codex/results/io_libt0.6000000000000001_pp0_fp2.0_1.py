import io.github.pactstart.mq.MessageSendService;
import io.github.pactstart.mq.MessageSender;
import io.github.pactstart.mq.serializer.DefaultMessageSerializer;
import io.github.pactstart.mq.serializer.MessageSerializer;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MessageSendServiceImpl implements MessageSendService {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    @Override
    public void sendMessage(MessageSender messageSender) {
        rabbitTemplate.convertAndSend(messageSender.getExchange(), messageSender.getRouteKey(), messageSender.getMessage(), message -> {
            if (messageSender.getDelayTimeLevel() > 0) {
                message.getMessageProperties().setExpiration(String.valueOf(messageSender.getDelayTimeLevel()
