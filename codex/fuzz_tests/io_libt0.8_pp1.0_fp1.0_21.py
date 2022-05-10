import io.netty.channel.ChannelPipeline;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.ssl.SslContext;
import io.netty.handler.ssl.SslContextBuilder;
import io.netty.handler.ssl.SslHandler;
import io.netty.handler.ssl.util.InsecureTrustManagerFactory;
import io.netty.handler.ssl.util.SelfSignedCertificate;
import jdk.nashorn.internal.ir.ReturnNode;

import javax.net.ssl.SSLEngine;
import java.io.IOException;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Created by zhugongyi on 2017/6/28.
 */
public class SslTest {

    static final boolean SSL = System.getProperty("ssl") != null;
    static final String HOST = System
