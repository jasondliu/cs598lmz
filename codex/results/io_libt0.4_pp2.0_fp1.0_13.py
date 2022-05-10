import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by wangyb on 2017/9/7.
 * 描述：
 */

public class AddFriendPresenter extends BasePresenter<IAddFriendView> {

    private static final String TAG = "AddFriendPresenter";

    public AddFriendPresenter(IAddFriendView view) {
        super(view);
    }

    public void searchFriend(String key) {
        HttpMethods.getInstance().getService(UserService.class)
                .searchFriend(key)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Consumer<BaseResponse<List<Friend>>>() {
                    @Override
                    public void accept(BaseResponse<List<Friend>> listBaseResponse) throws Exception {
                       
