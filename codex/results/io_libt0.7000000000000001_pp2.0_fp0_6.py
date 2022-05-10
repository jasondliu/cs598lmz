import io.reactivex.Observable;
import io.reactivex.ObservableSource;
import io.reactivex.ObservableTransformer;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.annotations.NonNull;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by zn.wang on 17/4/21.
 * 网络请求统一封装
 * 用的是retrofit的封装
 * 暂时不用
 */

public class RxNetUtil {

    private static final String TAG = "RxNetUtil";
    private static final String BASE_URL = "http://api.jisuapi.com/";
    private static final String KEY = "key";
    private static final
