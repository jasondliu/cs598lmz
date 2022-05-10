import io.netty.handler.codec.MessageToMessageCodec
import io.netty.handler.codec.binary.ByteArrayEncoder
import io.netty.handler.codec.http.websocketx.WebSocketClientProtocolHandler
import java.util.concurrent.CompletableFuture
import io.netty.channel.ChannelInboundHandlerAdapter as Adapter

private val logger: Logger = loggerFor()

/**
 * Channel for a channel for WebSocket and raw socket protocol with hybi-00, hybi-10 and hybi-17 subprotocols.
 */
class WSChannel(id: String, endpoint: String, client: WebSocketClient) : NettyChannel(id, endpoint, client, "ws") {

    private var delegatingCodec = false

    override fun newBootstrap(): Bootstrap {
        val wsBootstrap = super.newBootstrap()

        val pipeline = wsBootstrap.channel().pipeline()

        // Suspend reading because we need to test connection first
        pipeline.addBefore("decoder", "suspender", object : Adapter() {
           
