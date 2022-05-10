import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/11/24.
 */

public class MyPresenter extends BasePresenter<MyView> {
    private MyView myView;
    private MyModel myModel;

    public MyPresenter(MyView myView) {
        this.myView = myView;
        myModel = new MyModel();
    }

    public void getData(final String uid) {
        Observable<MyBean> observable = Observable.create(new ObservableOnSubscribe<MyBean>() {
            @Override
            public void subscribe(ObservableEmitter<MyBean> e) throws Exception {
                myModel.getData(uid, new MyModel.MyModel
