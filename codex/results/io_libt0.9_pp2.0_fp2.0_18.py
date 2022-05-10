import io.prestosql.testing.CloseableQueryRunner;
import io.prestosql.testing.LocalQueryRunner;
import io.prestosql.testing.MaterializedResult;
import io.prestosql.testing.MaterializedRow;
import io.prestosql.testing.QueryRunner;
import io.prestosql.testing.QueryRunnerFactory;
import io.prestosql.testing.materialize.MaterializedResultPrinter;

import java.nio.file.Paths;
import java.util.List;
import java.util.Optional;
import java.util.function.BiFunction;

import static io.prestosql.metadata.MetadataManager.createTestMetadataManager;
import static io.prestosql.spi.connector.ConnectorSession.Builder;
import static io.prestosql.spi.session.PropertyMetadata.integerSessionProperty;
import static io.prestosql.spi.type.BigintType.BIGINT;
import static io.prestosql.spi.type.DateType.
