import io.micronaut.context.annotation.Requires;
import io.micronaut.core.util.functional.ThrowingSupplier;
import io.micronaut.http.HttpRequest;
import io.micronaut.http.client.RxHttpClient;
import io.micronaut.http.client.annotation.Client;
import io.micronaut.javafx.JavaFxConfiguration;
import io.micronaut.retry.annotation.Retryable;

import javax.inject.Singleton;
import java.util.Map;

@Singleton
@Requires(property = JavaFxConfiguration.ENABLED, value = "true")
public class RestUtils {
    private final RxHttpClient httpClient;

    public RestUtils(@Client("${micronaut.application.name}") RxHttpClient httpClient) {
        this.httpClient = httpClient;
    }

    @Retryable
    public <R> R execute(HttpRequest<?> request, Class<R> responseType) {
        return execute(() -> httpClient
