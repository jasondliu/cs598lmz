import io.reactivex.Observable
import io.reactivex.ObservableSource
import io.reactivex.ObservableTransformer
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.disposables.Disposable
import io.reactivex.functions.Consumer
import io.reactivex.subjects.PublishSubject
import java.util.concurrent.TimeUnit

/**
 * @author: ym  作者 E-mail: 15622113269@163.com
 * date: 2018/11/19
 * desc: 基于Rx的Presenter封装,控制订阅的生命周期
 *
 */
open class RxPresenter<T : BaseView> : BasePresenter<T> {

    var mView: T? = null
        private set

    private var mCompositeDisposable: CompositeDisposable? = null

    private var mErrorHandler: RxErrorHandler? = null

    protected var mApplication: Application? =
