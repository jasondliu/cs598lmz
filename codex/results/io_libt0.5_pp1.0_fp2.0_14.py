import io.netty.handler.timeout.IdleStateEvent;
import io.netty.handler.timeout.IdleStateHandler;
import io.netty.util.concurrent.DefaultEventExecutorGroup;

import java.net.InetSocketAddress;
import java.util.concurrent.TimeUnit;

/**
 * Created by liuyang on 2016/9/9.
 */
public class NettyClient {
    private final static int PORT = 9999;
    private final static String HOST = "127.0.0.1";
    private final static int READ_IDEL_TIME_OUT = 4; // 读超时
    private final static int WRITE_IDEL_TIME_OUT = 5;// 写超时
    private final static int ALL_IDEL_TIME_OUT = 7; // 所有超时
    private static Bootstrap b;

    public static void main(String[] args) {
        b = new Bootstrap();
        EventLoopGroup workerGroup = new NioEventLoopGroup();
        try {
            b.
