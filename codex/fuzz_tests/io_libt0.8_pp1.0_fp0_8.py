import io.reactivex.subjects.Subject;

public class RxBus {
    private static volatile RxBus instance;
    private Subject<Object> mSubject;
    private HashMap<String, CompositeDisposable> mSubscriptionMap;

    public static RxBus getInstance() {
        if (instance == null) {
            synchronized (RxBus.class) {
                if (instance == null) {
                    instance = new RxBus();
                }
            }
        }
        return instance;
    }

    private RxBus() {
        mSubject = PublishSubject.create().toSerialized();
        mSubscriptionMap = new HashMap<>();
    }

    public void post(Object object) {
        mSubject.onNext(object);
    }

    public <T> Observable<T> toObservable(Class<T> type) {
        return mSubject.ofType(type);
    }

    public void addSubscription(Object o, Disposable disposable) {
        String key = o.getClass().getName();
        if (mSubscriptionMap.
