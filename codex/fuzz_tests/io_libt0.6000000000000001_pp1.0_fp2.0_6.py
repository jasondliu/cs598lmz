import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.disposables.Disposable;

public class BasePresenter<T extends BaseView> {

    protected T view;

    private CompositeDisposable compositeDisposable = new CompositeDisposable();

    public void setView(T view) {
        this.view = view;
    }

    public void addDisposable(Disposable disposable){
        compositeDisposable.add(disposable);
    }

    public void onDestroy(){
        compositeDisposable.clear();
    }
}
