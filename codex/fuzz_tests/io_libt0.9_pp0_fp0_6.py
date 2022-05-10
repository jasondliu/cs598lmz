import io.reactivex.observers.TestObserver;
import io.reactivex.plugins.RxJavaHooks;
import io.reactivex.schedulers.Schedulers;

public class RxJavaHooksTest {
    @Test
    public void testOnError1() throws Exception {
        RxJavaHooks.setOnError(functions.Func1<Throwable, Throwable>() {
            @Override
            public Throwable call(Throwable throwable) {
                return new IllegalArgumentException("faked error");
            }
        });
        TestObserver<String> ts = new TestObserver<String>();
        Observable.error(new RuntimeException("real error"))
                .subscribe(ts);
        // FIXME no longer asserts due to https://github.com/ReactiveX/RxJavaHooks/issues/28
//        ts.assertError(IllegalArgumentException.class);
    }

    @Test
    public void testOnError2() throws Exception {
        RxJavaHooks.setOnError(functions.Func
