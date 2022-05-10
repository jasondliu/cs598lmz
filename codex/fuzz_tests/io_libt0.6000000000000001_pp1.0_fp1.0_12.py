import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/12/22.
 */

public class BasePresenter<V extends IBaseView> {
    protected V view;

    public BasePresenter(V view) {
        this.view = view;
    }
    protected void addSubscribe(Disposable disposable){
        HttpManager.getInstance().addDisposable(disposable);
    }

    protected <T> void subscribe(Observable<T> observable, BaseObserver<T> observer){
        observable.subscribeOn(Schedulers.io())
                .unsubscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(observer);
    }
}
