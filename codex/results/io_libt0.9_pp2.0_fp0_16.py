import io.reactivex.Observable;
import io.reactivex.Observable.OnSubscribe;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.annotations.NonNull;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;

/**
 * Created by zhouxibing on 2018/12/10.
 */
public class RxJavaRequestUtil {
    private static final int REQUEST_CODE = 321;
    private static CompositeDisposable mCompositeDisposable = null;
    private static Disposable disposable;

    /**
     * 检查token返回是否失效，失效则必须刷新token后再进行其它操作
     * @param getTokenType  刷新Token的方式
