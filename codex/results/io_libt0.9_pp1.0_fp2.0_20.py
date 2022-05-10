import io.reactivex.Observable

/**
 * Created by Evandro on 20/03/2018.
 */

abstract class BasePresenter<T> constructor(protected var view: T) {

    fun getView(): T = view

    open fun start() {}

    open fun stop(){
        //CompositeDisposable().clear()
    }
}
