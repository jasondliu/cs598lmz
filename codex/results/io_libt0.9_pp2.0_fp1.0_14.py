import io.reactivex.disposables.Disposable;

/**
 * view层的base类
 *
 * @author fox
 * @since 2018/3/3
 */

public abstract class BaseView {

    private CompositeDisposable disposables;

    public Disposable subscribe(Observable observable, final ApiCallBack callBack) {
        if (disposables == null) {
            disposables = new CompositeDisposable();
        }

        Disposable disposable = observable.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Consumer<Object>() {
                    @Override
                    public void accept(Object obj) throws Exception {
                        if (callBack != null) {
                            callBack.onSuccess(obj);
                        }
                    }
                }, new Consumer<Throwable>() {
                    @Override
                    public void accept(Throwable throwable) throws Exception {
                        if (callBack != null) {
                            Log.e("RYAN", "throwable
