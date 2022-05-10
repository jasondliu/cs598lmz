import io.reactivex.Observable
import io.reactivex.ObservableSource
import io.reactivex.ObservableTransformer
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit

/**
 * Created by zhangxutong on 2018/1/1.
 */

class RxUtil {

    companion object {
        fun <T> rxSchedulerHelper(): ObservableTransformer<T, T> {    //compose简化线程
            return ObservableTransformer { observable ->
                observable.subscribeOn(Schedulers.io())
                        .observeOn(AndroidSchedulers.mainThread())
            }
        }

        fun <T> rxSchedulerHelper(delay: Long): ObservableTransformer<T, T> {    //compose简化线程
            return ObservableTransformer { observable ->
                observable
