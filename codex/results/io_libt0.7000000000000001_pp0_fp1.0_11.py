import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by zhang on 2017/9/18.
 */

public class MainPresenterImpl implements MainPresenter {

    private MainView mMainView;
    private Context mContext;
    public MainPresenterImpl(Context context) {
        mContext = context;
    }

    @Override
    public void attachView(MainView view) {
        mMainView = view;
    }

    @Override
    public void detachView() {
        mMainView = null;
    }

    @Override
    public void getDataFromNet(final String data) {
        Observable.create(new ObservableOnSubscribe<String>
