import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit

/**
 * Created by zhangxutong on 2017/12/25.
 */

class RxJavaTest {
    fun test() {
        Observable.create(ObservableOnSubscribe<Int> { e ->
            e.onNext(1)
            e.onNext(2)
            e.onNext(3)
            e.onComplete()
        }).subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(object : Observer<Int> {
                    override fun onSubscribe(d: Disposable) {
                        Log.e("TAG", "onSubscribe")
                    }

                    override fun onNext(value: Int) {
                        Log.e("TAG", "onNext:$value")
                    }

                    override fun onError(e:
