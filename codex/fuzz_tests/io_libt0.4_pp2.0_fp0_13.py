import io.reactivex.disposables.CompositeDisposable
import io.reactivex.disposables.Disposable
import io.reactivex.functions.Consumer
import io.reactivex.schedulers.Schedulers
import java.io.File
import java.util.*
import java.util.concurrent.TimeUnit

/**
 * Created by Administrator on 2018/2/1.
 */
class RecordPresenter(view: RecordContract.View) : RecordContract.Presenter {

    private var mView: RecordContract.View = view
    private val mCompositeDisposable: CompositeDisposable

    init {
        mView.setPresenter(this)
        mCompositeDisposable = CompositeDisposable()
    }

    override fun subscribe() {

    }

    override fun unSubscribe() {
        mCompositeDisposable.clear()
    }

    override fun startRecord() {
        val disposable = RxView.clicks(mView.getRecordButton())
                .throttleFirst(500, TimeUnit.MILL
