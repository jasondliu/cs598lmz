import io.netty.channel.ChannelPromise;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * @author Hinsteny
 * @Describtion
 * @date 2017/3/17
 * @copyright: 2016 All rights reserved.
 */
public class RpcClient extends SimpleChannelInboundHandler<RpcResponse> {

    private static final Logger logger = LoggerFactory.getLogger(RpcClient.class);

    private RpcResponse response;

    private final Object responseLock = new Object();

    private ChannelPromise promise;

    private Throwable cause;

    public RpcClient(ChannelPromise promise) {
        this.promise = promise;
    }

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, RpcResponse msg) throws Exception {
        this.response = msg;
        synchronized (responseLock) {
            responseLock.notifyAll();
        }
    }

    @Override
    public void channelReadComplete(ChannelHandlerContext ctx) throws Exception {
        ctx
