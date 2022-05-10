import io.vertx.core.json.JsonObject;

/**
 * Configuration for {@link io.vertx.ext.auth.authentication.AuthenticationProvider} implementations.
 *
 * @author <a href="http://tfox.org">Tim Fox</a>
 *
 * @deprecated Please use the {@link io.vertx.ext.auth.authentication} classes instead.
 */
@Deprecated
public interface AuthProviderOptions {

  @Deprecated
  static AuthProviderOptions options() {
    return new io.vertx.ext.auth.AuthProviderOptions();
  }

  @Deprecated
  static AuthProviderOptions options(JsonObject json) {
    return new io.vertx.ext.auth.AuthProviderOptions(json);
  }

  @Deprecated
  JsonObject toJson();

  /**
   * @return the name of the provider. It must corresponds to the name used in
   * {@link io.vertx.ext.auth.AuthService#registerProvider(String, AuthProvider)}
   */
  @Deprecated
  String getName();


