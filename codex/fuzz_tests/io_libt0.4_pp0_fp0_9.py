import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import retrofit2.HttpException;

public class LoginViewModel extends BaseViewModel {

    private MutableLiveData<Boolean> isLoading = new MutableLiveData<>();
    private MutableLiveData<Boolean> isLogin = new MutableLiveData<>();
    private MutableLiveData<String> error = new MutableLiveData<>();

    public LoginViewModel() {
    }

    public MutableLiveData<Boolean> getIsLoading() {
        return isLoading;
    }

    public MutableLiveData<Boolean> getIsLogin() {
        return isLogin;
    }

    public MutableLiveData<String> getError() {
        return error;
    }

    public void login(String username, String password) {
        isLoading.setValue(true);
        getCompositeDisposable().add(
                getDataManager().doLogin
