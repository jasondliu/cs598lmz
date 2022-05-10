import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2018/5/16.
 */

public class RxJavaUtils {

    public static void getObservable(final String path, final Map<String, String> map, final Class clazz, final MyCallBack callBack) {
        Observable<String> observable = Observable.create(new ObservableOnSubscribe<String>() {
            @Override
            public void subscribe(ObservableEmitter<String> e) throws Exception {
                String data = HttpUtils.getData(path, map);
                e.onNext(data);
            }
        });

        Observer<String> observer = new Observer<
