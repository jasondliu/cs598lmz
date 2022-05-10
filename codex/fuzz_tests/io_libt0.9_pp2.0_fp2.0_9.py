import io.rsocket.RSocket;
import io.rsocket.SocketAcceptor;
import io.rsocket.transport.netty.server.WebsocketRouteTransport;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@Slf4j
public class RSocketServerConfiguration {

    @Autowired
    private MetricsHandlerInterceptor metricsHandlerInterceptor;
    @Autowired
    private SocketAcceptor socketAcceptor;

    @Bean
    public Mono<CloseableChannel> rSocketServer() {
        return WebsocketRouteTransport.create(socketAcceptor)
                .start(TcpServerTransport.create("127.0.0.1", 7080));
    }

    @Bean
    public SocketAcceptor socketAcceptor() {
        return (setup, sendingSocket) -> Mono.just(new DefaultResponder
