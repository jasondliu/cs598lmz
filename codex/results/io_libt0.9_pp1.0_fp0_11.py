import io.vertx.core.shareddata.Counter;
import io.vertx.core.shareddata.SharedData;
import io.vertx.core.shareddata.impl.SharedDataImpl;
import io.vertx.core.spi.cluster.NodeSelector;
import io.vertx.core.spi.cluster.RegistrationInfo;
import io.vertx.core.spi.metrics.Metrics;
import io.vertx.core.spi.metrics.MetricsProvider;
import io.vertx.core.spi.metrics.MetricsRegistry;
import io.vertx.spi.cluster.zookeeper.MockZKCluster.ZKServer;
import io.vertx.spi.cluster.zookeeper.impl.ZKRegistrationInfo;
import io.vertx.spi.cluster.zookeeper.impl.ZKUtil;
import org.apache.curator.test.TestingServer;
import org.junit.Ignore;
import org.junit.Test;

import java.net
