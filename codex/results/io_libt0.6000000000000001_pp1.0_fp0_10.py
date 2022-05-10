import io.reactivex.Observable;

/**
 * Create by wangqingqing
 * On 2017/10/26 15:58
 * Copyright(c) 2017 世联行
 * Description
 */
public class UserModel implements UserContract.Model {

    @Override
    public Observable<UserEntity> getUserInfo(String userId) {
        return Api.getDefault().getUserInfo(userId);
    }
}
