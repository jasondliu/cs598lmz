import io.netty.channel.Channel;
import io.netty.channel.ChannelFuture;
import io.netty.handler.ssl.SslHandler;

import io.netty.util.internal.logging.InternalLogger;
import io.netty.util.internal.logging.InternalLoggerFactory;

import javax.net.ssl.SSLEngine;

import static io.netty.handler.ssl.OpenSsl.UNABLE_TO_CREATE_A_SSL_ENGINE;
import static io.netty.handler.ssl.OpenSsl.UNABLE_TO_PROCEED_WITH_RENEGOTIATION;
import static io.netty.util.internal.ObjectUtil.checkNotNull;

/**
 * Negotiates with the browser on whether to use SSL/TLS or not. Most of the code is taken from
 * <a href="http://google-openssl.googlecode.com/svn/trunk/include/openssl/ssl.h">
 *     http://google-openssl.googlecode.com/
