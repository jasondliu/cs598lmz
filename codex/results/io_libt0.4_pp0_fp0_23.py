import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit

/**
 * @author: ym  作者 E-mail: 15622113269@163.com
 * date: 2018/11/7
 * desc: RxJava工具类
 *
 */
object RxUtils {

    /**
     * 统一线程处理
     *
     * @param <T>
     * @return
    </T> */
    fun <T> rxSchedulerHelper(): ObservableTransformer<T, T> {    //compose简化线程
        return ObservableTransformer { upstream ->
            upstream.subscribeOn(Schedulers.io())
                    .observeOn(AndroidSchedulers.mainThread())
        }
    }

    /**
     * 统一返
