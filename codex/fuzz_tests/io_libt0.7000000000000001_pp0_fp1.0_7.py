import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.channel.socket.DatagramPacket;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.CharsetUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.InetSocketAddress;
import java.util.concurrent.TimeUnit;

/**
 * Created by panhuayu on 2018/9/4.
 */
public class UdpServerHandler extends SimpleChannelInboundHandler<DatagramPacket> {
    private static final Logger logger = LoggerFactory.getLogger(UdpServerHandler.class);
    private UdpServer udpServer;

    public UdpServerHandler(UdpServer udpServer) {
        this.udpServer = udpServer;
    }

    @Override
    public void channelActive(ChannelHandlerContext
