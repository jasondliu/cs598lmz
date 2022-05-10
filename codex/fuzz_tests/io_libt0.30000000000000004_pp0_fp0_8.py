import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.codec.http.HttpContent;
import io.netty.handler.codec.http.HttpHeaders;
import io.netty.handler.codec.http.HttpResponse;
import io.netty.handler.codec.http.LastHttpContent;
import io.netty.util.CharsetUtil;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;

/**
 * Created by zhongjian on 2017/5/8.
 */
public class HttpClientInboundHandler extends ChannelInboundHandlerAdapter {

    private CountDownLatch latch;

    private StringBuilder responseContent = new StringBuilder();

    public HttpClientInboundHandler(CountDownLatch latch) {
        this.latch = latch;
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        if (msg instanceof H
