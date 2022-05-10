import io.netty.channel.Channel;
import io.netty.handler.codec.http.websocketx.TextWebSocketFrame;
import io.netty.handler.codec.http.websocketx.WebSocketFrame;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Created by zhangxinwei on 2018/4/21.
 */
public class WebSocketChannelManager {
    private static final Logger logger = LoggerFactory.getLogger(WebSocketChannelManager.class);

    private static WebSocketChannelManager instance = null;

    private static final long A_DAY = 24 * 60 * 60;

    private static final int MAX
