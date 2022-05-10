import io.reactivex.Observable;
import io.reactivex.ObservableSource;
import io.reactivex.ObservableTransformer;
import io.reactivex.Single;
import io.reactivex.SingleSource;
import io.reactivex.SingleTransformer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Action;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2018/4/2 0002.
 */

public class RxHelper {
    /**
     * 创建单个请求
     *
     * @param <T>
     * @return
     */
    public static <T> SingleTransformer<T, T> rxSingle(final Context context) {
        return new SingleTransformer<T, T>() {

