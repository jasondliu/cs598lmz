import io.reactivex.functions.Consumer;
import io.reactivex.functions.Predicate;
import io.reactivex.schedulers.Schedulers;

/**
 * @author sun.bl
 * @version 1.0
 * @Date 2018-05-29
 * @Description
 */

public class SearchPresenter implements SearchContract.Presenter {
    private Activity activity;
    private SearchContract.View view;
    private DataManager dataManager;

    public SearchPresenter(Activity activity, SearchContract.View view) {
        this.activity = activity;
        this.view = view;
        this.dataManager = new DataManager(activity);
    }

    @Override
    public void subscribe() {
        view.initView();
        getHotWords();
    }

    @Override
    public void unSubscribe() {
        dataManager.disposable();
    }

    @Override
    public void addSearchHistory(String key) {
        if (StringUtils.isEmpty(key)) {
            return;
        }
        SearchHistoryDao search
