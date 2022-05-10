import io.reactivex.Observable
import io.reactivex.ObservableOnSubscribe
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import java.io.File
import java.io.FileOutputStream
import java.io.IOException

/**
 * Created by zhangliang on 2018/6/7.
 */
class DownloadUtils {

    companion object {

        fun download(url: String, filePath: String, fileName: String, listener: DownloadListener) {
            Observable.create(ObservableOnSubscribe<String> {
                val file = File(filePath)
                if (!file.exists()) {
                    file.mkdirs()
                }
                val file1 = File(file, fileName)
                if (file1.exists()) {
                    file1.delete()
                }
                file1.createNewFile()
                val fileOutputStream = FileOutputStream(file1)
                val responseBody = OkHttpUtils.getInstance
