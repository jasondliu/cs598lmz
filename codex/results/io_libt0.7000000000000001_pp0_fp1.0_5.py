import io.netty.util.internal.logging.InternalLoggerFactory;
import io.netty.util.internal.logging.JdkLoggerFactory;
import io.netty.util.internal.logging.Slf4JLoggerFactory;
import io.netty.util.internal.logging.Slf4JLoggerFactory2;
import io.netty.util.internal.logging.SpiLoader;
import io.netty.util.internal.logging.SpiLoader.SpiProvider;
import java.lang.reflect.Constructor;

public abstract class LoggerFactory {
    static final /* synthetic */ boolean $assertionsDisabled = false;
    private static volatile Constructor<? extends InternalLoggerFactory> defaultFactoryConstructor;
    static final InternalLoggerFactory defaultFactory = getDefaultFactory();
    static final SpiProvider spiProvider = SpiLoader.loadFirstAvailable(SpiProvider.class);

    static final class DefaultInitializationResult {
        final InternalLoggerFactory factory;
        final Throwable cause;

        DefaultInitializationResult(InternalLoggerFactory factory2
