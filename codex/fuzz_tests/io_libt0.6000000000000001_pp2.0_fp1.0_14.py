import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.Disposable
import io.reactivex.functions.Consumer
import io.reactivex.schedulers.Schedulers
import org.json.JSONObject
import java.util.*
import java.util.concurrent.TimeUnit

/**
 * Created by liang on 2017/12/13.
 */
class ControlPresenter(val mView: ControlContract.View) : ControlContract.Presenter {
    override fun sendOrder(order: String) {
        if (mView.isActive()) {
            mView.showLoading()
            val disposable = Observable.create<String> {
                val result = mView.getControlApi().sendOrder(order)
                val jsonObject = JSONObject(result)
                val error = jsonObject.optString("error")
                if (!TextUtils.isEmpty(error)) {
                    it.onError(Throwable(error))
                } else {

