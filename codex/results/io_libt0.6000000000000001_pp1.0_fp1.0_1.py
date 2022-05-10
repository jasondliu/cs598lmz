import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

import static com.google.common.base.Preconditions.checkNotNull;

public class SettingsPresenter implements SettingsContract.Presenter {

    private static final String TAG = SettingsPresenter.class.getSimpleName();

    private final SettingsContract.View mView;
    private final DataRepository mDataRepository;
    private final CompositeDisposable mCompositeDisposable;

    public SettingsPresenter(SettingsContract.View view, DataRepository dataRepository) {
        mView = checkNotNull(view, "view cannot be null!");
        mDataRepository = checkNotNull(dataRepository, "dataRepository cannot be null!");
        mCompositeDisposable = new CompositeDisposable();
        mView.setPresenter(this);
    }

    @Override
    public void subscribe() {
        loadSettings();
    }

   
