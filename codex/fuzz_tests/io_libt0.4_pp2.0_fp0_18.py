import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2018/3/28.
 */

public class MyPresenter {
    private IView iView;
    private final MyModel myModel;
    private Disposable d;

    public MyPresenter(IView iView) {
        this.iView = iView;
        myModel = new MyModel();
    }

    public void login(String mobile, String password) {
        myModel.login(mobile, password)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread
