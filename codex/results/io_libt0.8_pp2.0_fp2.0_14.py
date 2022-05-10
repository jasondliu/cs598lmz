import io.vertx.core.net.SocketAddress;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.runners.MockitoJUnitRunner;
import org.opendaylight.controller.remote.rpc.registry.RpcRegistry;
import org.opendaylight.controller.remote.rpc.registry.RpcRegistry.Messages.RpcMessage;
import org.opendaylight.controller.remote.rpc.registry.gossip.BucketStoreAccess;
import org.opendaylight.controller.remote.rpc.registry.gossip.BucketStoreAccessImpl;
import org.opendaylight.controller.remote.rpc.registry.gossip.FixedTimeRetryStrategy;
import org.opendaylight.controller.remote.rpc.registry.gossip.RetryStrategy;
import org.opendaylight.controller.remote.rpc.registry.gossip.RpcEndpoint;
import
