import io.reactivex.Observable;
import org.greenrobot.eventbus.EventBus;

import static com.example.administrator.rxjavaandretrofitsimple.mvpStandard.utils.Preconditions.checkNotNull;

/**
 * Created by Administrator on 2017/1/18 0018.
 */

public class BasePresenter<V extends IBaseView> implements IBasePresenter<V> {
    protected V mView;

    private CompositeDisposable mCompositeDisposable;
    private WeakReference<Context> mContext;

    public BasePresenter(V view) {
        attachView(view);
    }

    public BasePresenter(Context mContext) {
        this.mContext = new WeakReference<Context>(mContext);
    }

    @Override
    public V getView() {
        return mView;
    }

    @Override
    public void attachView(V view) {
        mView = view;
    }

    @Override
    public void detachView() {
        //取消网
