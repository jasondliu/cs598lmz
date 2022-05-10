import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.processors.FlowableProcessor;
import io.reactivex.processors.PublishProcessor;

/**
 * Created by Allen on 2017/7/20.
 * <p>
 *
 * @author Allen
 *         用于管理RxBus的事件和Rxjava相关代码的生命周期处理
 */

public class RxManager {

    private static volatile RxManager mInstance;
    public RxBus mRxBus = RxBus.getInstanceBus();
    /**
     * 管理rxbus订阅
     */
    private Map<String, Observable<?>> mObservables = new HashMap<>();
    /*管理Observables 和 Subscribers订阅*/
    private CompositeDisposable mCompositeSubscription = new CompositeDisposable();


