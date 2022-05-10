import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

import static com.example.administrator.myapplication.R.drawable.f;

/**
 * Created by Administrator on 2017/11/14.
 */

public class NewsPresenter extends BasePresenter<INewsView> {

    public NewsPresenter(INewsView iNewsView) {
        super(iNewsView);
    }

    public void loadNews(final int type, final int pageIndex){
        //获取View
        final INewsView iNewsView=getView();
        if(iNewsView==null){
            return;
        }
        //显示正在加载进度条
        iNewsView.show
