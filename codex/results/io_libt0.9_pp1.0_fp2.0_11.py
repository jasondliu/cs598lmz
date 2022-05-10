import io.micronaut.context.annotation.ConfigurationBuilder;
import io.micronaut.context.annotation.ConfigurationProperties;
import io.micronaut.context.annotation.ConfigurationReader;
import io.micronaut.context.annotation.Factory;
import io.micronaut.context.annotation.Parameter;
import io.micronaut.context.reader.ConfigurationPropertyNotFoundException;
import io.micronaut.context.reader.DefaultConfigurationReader;
import io.micronaut.context.scope.Refreshable;

import java.util.HashMap;
import java.util.Map;

/**
 * <p>
 * A {@link DefaultKeyValueMapper} that uses a {@link DefaultConfigurationReader} to initialize itself.
 * </p>
 * <p>
 * {@link Refreshable} instances invoke the refresh method when their refresh is triggered. This allows
 * the mapper to refresh the underlying configuration at runtime.
 * </p>
 *
 * @author Graeme Rocher
 * @since 1.0
 */
@ConfigurationProperties
@Factory

