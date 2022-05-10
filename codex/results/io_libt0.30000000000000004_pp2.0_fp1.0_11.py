import io.reactivex.Observable;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/3/24.
 */

public class MyPresenter extends BasePresenter<MyContract.View> implements MyContract.Presenter {

    private MyContract.View view;
    private MyContract.Model model;

    public MyPresenter(MyContract.View view) {
        this.view = view;
        model = new MyModel();
    }

    @Override
    public void getDataFromNet(String url) {
        Observable<MyBean> myBean = model.getDataFromNet(url);
        myBean.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<MyBean>() {
                    @Override
                    public void onSubscribe(
