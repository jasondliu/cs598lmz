import io.remme.java.webSocket.dto.SubscribeMessage;
import io.remme.java.webSocket.dto.SubscribePayload;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;

import java.net.URI;
import java.net.URISyntaxException;

/**
 * Java bindings for Remme WebSockets.
 * It allows you to open a connection to the Remme WebSocket service.
 */
@Slf4j
public class RemmeWebSocketClient {
    public static final String DEFAULT_URL = "wss://testnet-socket.remme.io/subscribe";
    public static final String SOCKET_BATCH_BLOCK = "batch_block_info";
    public static final String SOCKET_SEND_TRANSACTION = "send_transaction";
    public static final String SOCKET_MEMBERSHIP = "membership";

    private WebSocketClient webSocketClient;
    @Setter
    private IWebSocketCallback onOpenCallback;
    @
