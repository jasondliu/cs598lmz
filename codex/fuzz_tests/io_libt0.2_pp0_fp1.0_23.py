import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/11/29.
 */

public class MyPresenter extends BasePresenter<IMyView> {

    private MyModel myModel;

    public MyPresenter(IMyView iMyView) {
        super(iMyView);
    }

    @Override
    protected void initModel() {
        myModel = new MyModel();
    }

    public void getData(String uid) {
        myModel.getData(uid)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<MyBean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                   
