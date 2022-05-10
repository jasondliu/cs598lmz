import io.reactivex.disposables.Disposable;
import io.reactivex.observers.DisposableObserver;

/**
 * Created by shenmingnan on 2018/4/24.
 */

public abstract class ErrorHandlerObserver<T> extends DisposableObserver<T> {

    @Override
    public void onNext(T t) {
        if (null != t) {
            onSuccess(t);
        }
    }

    @Override
    public void onError(Throwable e) {
        onFail(ExceptionEngine.handleException(e));
    }

    @Override
    public void onComplete() {

    }

    // 正常返回
    public abstract void onSuccess(T t);

    // 异常返回
    public abstract void onFail(ApiException exception);
}
