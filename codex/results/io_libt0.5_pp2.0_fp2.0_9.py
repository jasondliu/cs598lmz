import io.netty.handler.codec.http.websocketx.WebSocketServerProtocolHandler;
import io.netty.handler.stream.ChunkedWriteHandler;
import io.netty.handler.timeout.IdleStateHandler;

import java.util.Map;
import java.util.concurrent.TimeUnit;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

import com.jzfq.retail.core.call.domain.CallLog;
import com.jzfq.retail.core.call.service.CallLogService;
import com.jzfq.retail.core.config.NettyProperties;
import com.jzfq.retail.core.config.RedisKeyPrefix;
import com.jzfq.retail.core.service
