import io.reactivex.Observable;

/**
 * Created by Administrator on 2017/4/14.
 */

public interface IUserModel {
    Observable<User> getUser(String userName, String userPwd);
}
