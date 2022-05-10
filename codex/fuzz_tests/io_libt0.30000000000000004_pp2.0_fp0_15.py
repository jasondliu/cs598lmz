import io.reactivex.Observable
import io.reactivex.ObservableEmitter
import io.reactivex.ObservableOnSubscribe
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import java.io.File
import java.io.FileOutputStream
import java.io.IOException
import java.io.InputStream
import java.net.URL
import java.net.URLConnection

/**
 * Created by zhangli on 2018/6/29.
 */
class DownloadUtils {

    companion object {
        val instance: DownloadUtils by lazy(mode = LazyThreadSafetyMode.SYNCHRONIZED) {
            DownloadUtils()
        }
    }

    fun download(url: String, filePath: String, fileName: String, listener: DownloadListener): Observable<Int> {
        return Observable.create(ObservableOnSubscribe<Int> { emitter ->
            var inputStream: InputStream? = null
            var outputStream: File
