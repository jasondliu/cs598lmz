import io.reactivex.Observable;

/**
 * Created by jian.shui on 2018/11/29
 */
public class UserModel {
    private UserApi userApi;
    public UserModel(){
        userApi= HttpManager.getInstance().getUserApi();
    }
    public Observable<UserInfo> getUserInfo(String userId){
        return userApi.getUserInfo(userId);
    }
}
