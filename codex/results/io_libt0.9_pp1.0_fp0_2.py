import io.siddhi.core.util.collection.executor.CollectionExecutor;
import io.siddhi.core.util.config.ConfigReader;
import io.siddhi.core.util.statistics.LatencyTracker;
import io.siddhi.core.util.statistics.ThroughputTracker;
import io.siddhi.core.util.statistics.metrics.Level;
import io.siddhi.core.util.statistics.metrics.MetricLabel;
import io.siddhi.query.api.definition.Attribute;

import java.util.Iterator;
import java.util.List;

/**
 * Implementation to {@link CollectionExecutor} which behaves like head(*,N) on in-memory table.
 */
@Extension(
        name = "indexed",
        namespace = "collection",
        description = "Returns the head elements of the collection with index",
        parameters = {
                @Parameter(name = "id",
                        description = "The index of the element that needs to be retreived from the collection.",
                        type = {Data
