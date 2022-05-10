import io.vertx.core.Handler;
import io.vertx.core.Verticle;
import io.vertx.core.Vertx;
import io.vertx.core.buffer.Buffer;
import io.vertx.core.http.HttpClient;
import io.vertx.core.http.WebSocketFrame;
import io.vertx.core.json.JsonObject;
import io.vertx.core.net.NetClient;
import io.vertx.core.net.NetClientOptions;
import io.vertx.core.net.NetSocket;
import io.vertx.core.windowing.Window;
import io.vertx.core.windowing.Windowing;

import java.util.HashMap;
import java.util.Map;

/**
 * This verticle will establish a websocket connection to the web client and serve as a connection between all different
 * services. It will be used to deliver notifications to the web client and provide a means to call the other events
 * from the web client.
 */
public class WebSocketVerticle implements Verticle {

	private Vertx vert
