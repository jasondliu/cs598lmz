import io.reactivex.Flowable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

public class ExponentialBackOffStrategy implements BackOffStrategy {

    //linear back off params
    private final int initialIntervalMillis = 1000;
    private final int maxIntervalMillis = 32000;
    private final float multiplier = 1.5f;

    @Override
    public Single<Object> getBackOffAwait(RxBus rxBus) {
        return Single.create(
                e -> {
                    final Flowable<Object> ref = rxBus.toFlowable(Object.class);

                    //Event received from cache
                    final Consumer<Object> whenNext = gsonData -> {
                        if (gsonData != null) {
                            e.onSuccess(gsonData);
                        }
                    };

                    //Error while event received from cache
                    final Consumer<Throwable> whenError = error -> {
                        e.onError(error);
                    };

                    //Event error after exponential back off
