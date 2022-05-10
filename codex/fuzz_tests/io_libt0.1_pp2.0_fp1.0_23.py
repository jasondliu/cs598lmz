import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.codec.http.HttpContent;
import io.netty.handler.codec.http.HttpHeaders;
import io.netty.handler.codec.http.HttpResponse;
import io.netty.handler.codec.http.LastHttpContent;
import io.netty.util.CharsetUtil;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * @author: wangjunchao(王俊超)
 * @date: 2019-01-09 11:01:01
 **/
public class HttpClientInboundHandler extends ChannelInboundHandlerAdapter {
    private final AtomicInteger counter;

    public HttpClientInboundHandler(AtomicInteger counter) {
        this.counter = counter;
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        if (msg instanceof HttpResponse) {
            HttpResponse
