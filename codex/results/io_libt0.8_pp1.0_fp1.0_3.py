import io.reactivex.observers.DisposableSingleObserver;
import io.reactivex.schedulers.Schedulers;

public class SingleViewModel extends ViewModel {

    private MutableLiveData<String> result = new MutableLiveData<>();
    private DisposableSingleObserver<String> disposableSingleObserver;

    public LiveData<String> getResult() {
        return result;
    }

    public void initialize(){
        disposableSingleObserver = getSingleObserver();
        Single.just(generateString())
                .subscribeOn(Schedulers.io())
                .subscribe(disposableSingleObserver);
    }

    @NonNull
    private DisposableSingleObserver<String> getSingleObserver() {
        return new DisposableSingleObserver<String>() {
            @Override
            public void onSuccess(String s) {
                result.setValue(s);
            }

            @Override
            public void onError(Throwable e) {

            }
        };
    }

    private String generate
