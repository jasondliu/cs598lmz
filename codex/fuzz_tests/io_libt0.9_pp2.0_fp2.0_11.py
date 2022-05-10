import io.reactivex.Maybe;
import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.schedulers.Schedulers;
import io.reactivex.subjects.PublishSubject;
import lombok.Getter;

/**
 * Created by xiaofei on 2017/6/5.
 */

public class RxBus {
    private static final String TAG = "RxBus";

    @Getter
    private final PublishSubject<Object> bus;

    @Getter
    private Map<Class<?>, Object> stickyEventMap;

    @Getter
    private CompositeDisposable compositeDisposable;

    public RxBus() {
        bus = PublishSubject.create();
        stickyEventMap = new ConcurrentHashMap<>();
        compositeDisposable = new CompositeDisposable();
    }

    /**
    
