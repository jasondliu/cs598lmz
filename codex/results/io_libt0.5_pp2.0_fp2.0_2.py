import io.netty.util.CharsetUtil;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicLong;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 *
 * @author mrashid
 */
public class ClientChannelInboundHandler extends ChannelInboundHandlerAdapter {

    private static final Logger logger = LoggerFactory.getLogger(ClientChannelInboundHandler.class);

    private final AtomicLong totalBytesRead = new AtomicLong();
    private final AtomicLong totalBytesWritten = new AtomicLong();
    private final AtomicLong totalMessagesRead = new AtomicLong();
    private final AtomicLong totalMessagesWritten = new AtomicLong();
    private final AtomicLong totalMessagesSent = new AtomicLong();
    private final AtomicLong totalMessagesReceived = new AtomicLong();
    private final AtomicLong
