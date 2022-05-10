import io.reactivex.Observable;
import io.reactivex.ObservableSource;
import io.reactivex.ObservableTransformer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.annotations.NonNull;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Action;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/12/6.
 */

public class BasePresenter<V extends BaseView> {

    private V mView;
    private CompositeDisposable mCompositeDisposable;

    public BasePresenter(V view) {
        mView = view;
    }

    public void detachView() {
        mView = null;
        unSubscribe();
    }

    public V getView() {
        return mView;
    }

    public void addSubscribe(Disposable
