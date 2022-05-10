import io.reactivex.Observable;

/**
 * Created by slb on 2018/6/4.
 */

public class SearchModel implements SearchContract.Model {
    @Override
    public Observable<SearchBean> getSearchBean(String key, String page, String size) {
        return RetrofitUtils3.getRetrofitService(MyApi.class).getSearchBean(key,page,size);
    }
}
