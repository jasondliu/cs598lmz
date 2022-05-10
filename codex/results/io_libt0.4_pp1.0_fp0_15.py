import io.netty.channel.ChannelHandlerContext;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * @author szh 2020/7/14
 */
public class ClientHandler extends SimpleChannelInboundHandler<String> {

    private final ExecutorService executorService;

    public ClientHandler() {
        executorService = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());
    }

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, String msg) throws Exception {
        executorService.submit(() -> {
            System.out.println("client receive msg:" + msg);
            ctx.writeAndFlush("client send msg:" + msg);
        });
    }
}
