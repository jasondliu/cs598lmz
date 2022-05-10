import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by sakkeer on 14/02/18.
 */

public class LoginPresenter implements LoginContract.Presenter {

    private LoginContract.View view;
    private LoginRepository loginRepository;

    public LoginPresenter(LoginContract.View view, LoginRepository loginRepository){
        this.view = view;
        this.loginRepository = loginRepository;
    }

    @Override
    public void checkLogin(String userName, String password) {
        loginRepository.checkLogin(userName, password)
                .subscribeOn(Schedulers.computation())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<Boolean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(Boolean aBoolean) {
                        if (aBoolean){
                
