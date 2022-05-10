import io.pravega.test.system.framework.services.Service;
import lombok.extern.slf4j.Slf4j;
import mesosphere.marathon.client.MarathonException;
import org.apache.zookeeper.KeeperException;
import org.junit.*;

import java.net.URI;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.stream.Collectors;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;

@Slf4j
public class FailoverTest extends AbstractFailoverTests {

    private PravegaControllerService controllerInstance1;
    private PravegaControllerService controllerInstance2;
    private PravegaControllerService controllerInstance3;
    private ZookeeperService zk1;
    private ZookeeperService zk2;
    private PravegaSegmentStore
