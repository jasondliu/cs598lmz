import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

public class MyOrderViewModel extends ViewModel {

    private MutableLiveData<List<MyOrderItem>> myOrderItemMutableLiveData;
    private CompositeDisposable compositeDisposable = new CompositeDisposable();
    private MyOrderRepository myOrderRepository;

    public MyOrderViewModel() {
        myOrderRepository = MyOrderRepository.getInstance();
    }

    public MutableLiveData<List<MyOrderItem>> getMyOrderItemMutableLiveData() {
        if (myOrderItemMutableLiveData == null) {
            myOrderItemMutableLiveData = new MutableLiveData<>();
        }
        getMyOrderItem();
        return myOrderItemMutableLiveData;
    }

    private void getMyOrderItem() {
        compositeDispos
