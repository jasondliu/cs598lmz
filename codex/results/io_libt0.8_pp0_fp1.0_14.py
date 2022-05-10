import io.r2dbc.postgresql.PostgresqlConnectionConfiguration;
import io.r2dbc.postgresql.PostgresqlConnectionFactory;
import io.r2dbc.postgresql.codec.JsonCodec;
import io.r2dbc.spi.ConnectionFactoryOptions;
import io.r2dbc.spi.ValidationDepth;

public class DatabaseConfiguration {

    private static final Logger log = LoggerFactory.getLogger(OAuth2DatabaseServerAutoConfiguration.class);
    private final ConnectionFactory connectionFactory;

    public DatabaseConfiguration(OAuth2DatabaseServerProperties databaseProperties) {
        this.connectionFactory = getConnectionFactory(databaseProperties);
    }

    private ConnectionFactory getConnectionFactory(OAuth2DatabaseServerProperties databaseProperties) {
        PostgresqlConnectionConfiguration configuration = PostgresqlConnectionConfiguration.builder()
                .host(databaseProperties.getHost())
                .port(databaseProperties.getPort())
                .database(databaseProperties.getDatabase())
                .username(databaseProperties.getUsername())

