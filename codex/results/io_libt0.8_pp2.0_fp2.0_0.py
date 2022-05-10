import io.reactivex.schedulers.Schedulers
import retrofit2.Retrofit
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory
import retrofit2.converter.gson.GsonConverterFactory
import java.lang.Exception
import java.lang.ref.WeakReference

object ApiManager {

    private val TAG = ApiManager::class.java.simpleName
    private var requestQueue: RequestQueue? = null
    private var mNetworkRequest: WeakReference<NetworkRequest>? = null
    private var mNetworkResponse: WeakReference<NetworkResponse>? = null
    private var mResponse: WeakReference<Response>? = null
    private val mHeader = HashMap<String, String>()

    init {
        mHeader.put("Accept-Version", BuildConfig.API_VERSION)
        mHeader.put("Content-Type", "application/json")
        mHeader.put("Accept", "application/json")
        mHeader.put("sutta", "true")
    }

    fun init(context: Context
