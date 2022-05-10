import io.reactivex.Observable;

/**
 * Created by Administrator on 2017/12/14 0014.
 */

public interface ICollectModel {
    Observable<CollectBean> getCollectList(String token, String type, int limit, int page);
}
