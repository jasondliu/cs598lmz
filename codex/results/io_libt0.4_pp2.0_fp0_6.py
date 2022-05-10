import io.reactivex.Observable;
import io.reactivex.functions.Function;

/**
 * Created by kang on 2017/3/10.
 */

public class DataManager {
    private static DataManager mDataManager;
    private final RetrofitService mRetrofitService;

    private DataManager() {
        mRetrofitService = RetrofitHelper.getInstance().getServer();
    }

    public static DataManager getInstance() {
        if (mDataManager == null) {
            synchronized (DataManager.class) {
                if (mDataManager == null) {
                    mDataManager = new DataManager();
                }
            }
        }
        return mDataManager;
    }

    public Observable<GankHttpResponse<List<GankItemBean>>> getGirlList(int num, int page) {
        return mRetrofitService.getGirlList(num, page);
    }

    public Observable<GankHttpResponse<List<GankItemBean>>> getRandomGirl(int num) {
        return mRetrofitService.
