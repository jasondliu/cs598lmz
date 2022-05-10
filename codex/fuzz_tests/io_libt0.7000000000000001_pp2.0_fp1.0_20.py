import io.netty.handler.codec.http.HttpVersion;
import io.netty.handler.codec.http.websocketx.*;
import io.netty.util.CharsetUtil;
import org.json.JSONObject;

import java.util.List;
import java.util.Map;
import java.util.Set;

public class WsClientHandler extends SimpleChannelInboundHandler<Object> {
    private WebSocketClientHandshaker handshaker;
    private ChannelPromise handshakeFuture;
    private boolean isLogin = false;
    private String userId;
    private String username;
    private String password;
    private String sessionId;
    private String serverUrl;
    private String serverIp;
    private int serverPort;
    private String clientId;
    private String clientName;
    private String clientVersion;
    private String clientType;
    private String clientMac;
    private String clientIp;
    private String clientLongitude;
    private String clientLatitude;
    private String clientDesc;
    private String clientStatus;
   
