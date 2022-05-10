import io.reactivex.Maybe;
import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;

/**
 * Created by liusheng on 16-11-17.
 */

public class YourWellComeWithPackPresenter extends BasePresenter<YourWellComeWithPackView, YourWellComeWithPackModelImpl> {

    private String TAG = "YourWellComeWithPackPresenter";
    private long saleableCount = 0;
    private RoomDetailEntity roomDetailEntity;

    public YourWellComeWithPackPresenter(YourWellComeWithPackView view) {
        super(view);
    }

    @Override
    protected YourWellComeWithPackModelImpl createModel() {
        return new YourWellComeWithPackModelImpl();
    }

    public void initYourWellcome(long id) {

        getModel().getYourWellCome(id)
                .subscribeOn(Schedulers.io())
                .observeOn(Schedulers.io())
                .flatMap(new Function<YourWellComeEntity, Maybe<List<
