import io.vertx.core.json.JsonObject;
import io.vertx.core.logging.Logger;
import io.vertx.core.logging.LoggerFactory;

import java.io.IOException;
import java.io.OutputStream;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class MessageHandler implements Handler<Message<JsonObject>> {

    private static final Logger LOG = LoggerFactory.getLogger(MessageHandler.class);

    private final Map<String, OutputStream> outputStreams = new HashMap<>();

    private final Random random = new Random();

    private final String[] lines = new String[60];

    {
        for (int i = 0; i < lines.length; i++) {
            lines[i] = Integer.toString(i);
        }
    }

    @Override
    public void handle(Message<JsonObject> event) {
        JsonObject message = event.body();

        switch (message.getString("action")) {
            case
