import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by zzj on 2017/10/20.
 */

public class RankDataManager {

    private static volatile RankDataManager instance;

    public static RankDataManager getInstance(){
        if (instance==null){
            synchronized (RankDataManager.class){
                if (instance==null){
                    instance=new RankDataManager();
                }
            }
        }
        return instance;
    }

    //查询用户排行榜数据
    public Subscription getRankList(RxAppCompatActivity rxAppCompatActivity, Map<String,String> params, ResponseListener<RankResult> listener){
        return ApiUtil.getInstance().getApiService().getRankList(params)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(
