import io.reactivex.Observable;
import io.reactivex.Single;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;
import io.reactivex.observers.DisposableSingleObserver;
import io.reactivex.schedulers.Schedulers;
import io.reactivex.subjects.PublishSubject;

public class MainViewModel extends ViewModel {

    private static final String TAG = MainViewModel.class.getSimpleName();

    private final Repository repository;
    private final PublishSubject<String> searchSubject = PublishSubject.create();
    private final PublishSubject<String> errorSubject = PublishSubject.create();
    private final PublishSubject<Boolean> progressSubject = PublishSubject.create();
    private final PublishSubject<Boolean> isOfflineSubject = PublishSubject.create();

    private Disposable disposable;

    public MainViewModel(Repository repository) {
        this.repos
