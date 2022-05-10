import io.reactivex.Observable;
import io.reactivex.ObservableSource;
import io.reactivex.ObservableTransformer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;

/**
 * @author sgfb
 * @e-mail sgfbitom@qq.com
 * @time 2017/11/6
 * @desc
 * @version
 */
public abstract class BasePresenter<V extends IView> implements IPresenter<V>{

    private CompositeDisposable mCompositeDisposable;
    private V mView;

    public BasePresenter(V view){
        mView = view;
    }

    @Override
    public void attachView(V view) {
        mView = view;
    }
