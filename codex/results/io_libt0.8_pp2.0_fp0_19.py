import io.vertx.core.Vertx;
import io.vertx.core.buffer.Buffer;
import io.vertx.core.eventbus.MessageCodec;
import io.vertx.core.json.JsonArray;
import io.vertx.core.json.JsonObject;

public class JsonArrayMessageCodec implements MessageCodec<JsonArray, JsonArray> {

  @Override
  public void encodeToWire(final Buffer buffer, final JsonArray jsonArray) {
    final String jsonToStr = jsonArray.encode();
    final byte[] encoded = jsonToStr.getBytes(StandardCharsets.UTF_8);
    buffer.appendInt(encoded.length);
    buffer.appendBytes(encoded);
  }

  @Override
  public JsonArray decodeFromWire(final int position, final Buffer buffer) {
    final int length = buffer.getInt(position);
    final byte[] encoded = buffer.getBytes(position + 4, position + 4 + length);
    final String str = new String(encoded, StandardCharsets.UTF_
