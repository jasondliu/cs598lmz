import io.noties.debug.IWatch;
import io.noties.debug.LeakCanaryProxy;
import io.noties.debug.RefWatcher;
import io.noties.debug.RefWatcherDebug;

public class RefWatcherTest extends BaseTest {

    public void test_no_dynamic_proxy() {

        final IWatch watch = mock(IWatch.class);

        final RefWatcher refWatcher = new RefWatcher(watch, new RefWatcher.Config.Builder()
                .dynamicProxy(false)
                .build());

        final Dummy dummy = new Dummy();
        refWatcher.watch(dummy);
        refWatcher.watch(mock(Dummy.class));

        final Object object = new Object();
        final Object object2 = new Object();
        refWatcher.watch(object);
        refWatcher.watch(object2);

        refWatcher.watchAll(Arrays.asList(object, object2));

        verify(watch).watch(dummy);
        verify(watch, never()).watch(any(Dummy
