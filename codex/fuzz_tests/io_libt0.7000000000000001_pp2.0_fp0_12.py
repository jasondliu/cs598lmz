import io.vertx.core.buffer.Buffer;
import io.vertx.core.http.HttpServerResponse;
import io.vertx.ext.web.RoutingContext;

import java.io.IOException;

public class PUTHandler extends AbstractHandler {


    public PUTHandler(Vertx vertx) {
        super(vertx);
    }

    @Override
    public void handle(RoutingContext routingContext) {
        HttpServerResponse response = routingContext.response();
        try {
            Buffer buffer = routingContext.getBody();
            byte[] bytes = buffer.getBytes();
            FileHelper.writeFile(bytes);
            response.setStatusCode(200);
            response.putHeader("content-type", "text/plain");
            response.end("OK");
        } catch (IOException e) {
            response.setStatusCode(500);
            response.putHeader("content-type", "text/plain");
            response.end(e.getMessage());
        }
    }
}
