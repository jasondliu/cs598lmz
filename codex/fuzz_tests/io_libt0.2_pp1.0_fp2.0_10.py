import io.reactivex.Observable;
import io.reactivex.ObservableSource;
import io.reactivex.ObservableTransformer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.annotations.NonNull;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;
import okhttp3.ResponseBody;

/**
 * Created by Administrator on 2017/8/10.
 */

public class MainPresenter extends BasePresenter<MainView> {
    public MainPresenter(MainView view) {
        super(view);
    }

    public void getData(String url) {
        view.showLoading();
        addDisposable(
                RetrofitHelper.getInstance().getApiService().getData(url)
                        .compose(new ObservableTransformer<ResponseBody, String>
