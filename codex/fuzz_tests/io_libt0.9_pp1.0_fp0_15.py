import io.reactivex.annotations.NonNull;

/**
 * @author : yzw
 * @date : 2019/4/4
 */
public class ResultError {

    private NetError mNetError;

    public ResultError(@NonNull NetError mNetError) {
        this.mNetError = mNetError;
    }

    public NetError getError() {
        return mNetError;
    }
}
