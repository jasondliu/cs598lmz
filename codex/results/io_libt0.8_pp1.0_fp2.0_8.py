import io.reactivex.disposables.CompositeDisposable
import io.reactivex.disposables.Disposable

/**
 * Created by tiny on 11/22/17.
 */
class BasePresenter<V : MvpView> : MvpPresenter<V> {

    var compositeDisposable = CompositeDisposable()

    var view: V? = null

    override fun attachView(view: V) {
        this.view = view
    }

    override fun detachView() {
        compositeDisposable.dispose()
        this.view = null
    }

    override fun detachView(disposable: Disposable?) {
        disposable?.let {
            compositeDisposable.remove(it)
            compositeDisposable.dispose()
        }
    }
}
