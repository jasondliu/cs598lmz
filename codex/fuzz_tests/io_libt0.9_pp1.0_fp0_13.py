import io.vertx.core.json.JsonArray;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class ConnectionHandler<R, S> {

  private static final Logger log = LoggerFactory.getLogger(ConnectionHandler.class);

  static Class<?> checkType(MethodHandle handle, Class<?> type) throws IllegalAccessException {
    Class<?> ret = handle.type().parameterType(0);
    if (ret != type) {
      throw ConstructorException.INSTANCE.failure(String.format("Expected %s type", type.getName()));
    }
    return ret;
  }

  static void checkArgument(MethodHandle handle) throws IllegalAccessException {
    MethodType type = handle.type();
    if (type.parameterCount() != 1) {
      throw ConstructorException.INSTANCE.failure("Expecting only the JsonObject argument for @WSMessage");
    }
  }

  static MethodHandle getGetter(Me
