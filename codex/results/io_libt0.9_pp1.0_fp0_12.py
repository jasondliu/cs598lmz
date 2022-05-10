import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;

public class SearchModel implements SearchContract.Model {
    @Override
    public Disposable searchFood(final RequestCallBack callBack,String name) {
        final ApiService apiService = ApiService.getInstance();
        Observable<SearchBean> observable = apiService.searchFood(name);
        Disposable subscribe = observable.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Consumer<SearchBean>() {
                    @Override
                    public void accept(SearchBean searchBean) throws Exception {
                        callBack.onNext(searchBean);
                    }
                }, new Consumer<Throwable>() {
                    @Override
                    public void accept(Throwable throwable) throws Exception {
                        callBack.onError(throwable.getMessage());
                    }
                });

