import io.reactivex.Observable;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import okhttp3.ResponseBody;

/**
 * Created by Administrator on 2017/6/21.
 */

public class SearchPresenter extends BasePresenter<SearchContract.View> implements SearchContract.Presenter {

    private SearchContract.View view;
    private SearchContract.Model model;
    private Context context;

    public SearchPresenter(SearchContract.View view, Context context) {
        this.view = view;
        this.context = context;
        model = new SearchModel();
    }

    @Override
    public void getSearchData(String key, int page, int count) {
        Observable<SearchBean> searchData = model.getSearchData(key, page, count);
        searchData.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.
