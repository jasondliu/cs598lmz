import io.netty.handler.codec.http.HttpHeaderNames;

/**
 * Request 工具类
 *
 * @author hanliang
 * @version 1.0
 * @date 2019/7/10 11:38
 */
public class RequestUtils {
    /**
     * 获取请求客户端ip
     *
     * @param ctx
     * @return
     */
    public static String getRemoteIp(ChannelHandlerContext ctx) {
        String ip = ctx.channel().remoteAddress().toString();
        if (ip.contains("/")) {
            ip = ip.substring(ip.lastIndexOf("/") + 1, ip.length());
        }
        if (ip.contains(":")) {
            ip = ip.substring(0, ip.lastIndexOf(":"));
        }
        return ip;
    }

    /**
     * 获取请求客户端端口
     *
     * @
