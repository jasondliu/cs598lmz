import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers

/**
 * Created by zq on 2017/11/22.
 */
class MainPresenter(context: Context, view: MainContract.View) : MainContract.Presenter {

    var mContext: Context? = null
    var mView: MainContract.View? = null
    val mModel: MainModel by lazy {
        MainModel()
    }

    init {
        mView = view
        mContext = context
    }

    override fun start() {
        requestData()
    }

    override fun requestData() {
        val observable: Observable<ArrayList<AndroidBean>>? = mContext?.let { mModel.loadData(it, 10, 1) }
        observable?.subscribeOn(Schedulers.io())
                ?.observeOn(AndroidSchedulers.mainThread())
                ?.subscribe(object : Observer<ArrayList<
