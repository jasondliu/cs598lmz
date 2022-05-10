import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Function;
import io.reactivex.functions.Predicate;
import io.reactivex.plugins.RxJavaPlugins;
import io.reactivex.schedulers.Schedulers;
import io.reactivex.subjects.PublishSubject;
import io.reactivex.subjects.ReplaySubject;

public class RxBus implements Bus {

    public static final int CACHE = 0;
    public static final int RELAY = -1;
    private static RxBus instance;

    private final Map<Class<?>, Object> stickyEventsMap;

    public RxBus() {
        stickyEventsMap = new ConcurrentHashMap<>();
    }

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

    private Map<Class<?
