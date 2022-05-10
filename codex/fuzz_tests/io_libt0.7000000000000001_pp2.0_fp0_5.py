import io.reactivex.Observable;

/**
 * Created by Administrator on 2018/3/28.
 */

public interface ISearchPresenter extends IBasePresenter {
    void getSearchHot(int id);
    Observable<SearchBean> getSearchTag(String tag);
}
