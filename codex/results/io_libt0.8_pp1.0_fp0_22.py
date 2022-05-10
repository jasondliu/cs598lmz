import io.reactivex.Observable;

public class ProductDetailsViewModel extends BaseViewModel {

    private final ProductApiService productApiService = new ProductApiService();

    public ProductDetailsViewModel(@NonNull Application application) {
        super(application);
    }

    public Observable<Product> getProductDetails(String productId) {
        Product product = new Product();

        product.name = "Product 1";
        product.tags.add("Tag 1");
        product.tags.add("Tag 2");
        product.tags.add("Tag 3");

        return Observable.just(product);
        /*return productApiService.getProductDetails(productId)
                .doOnError(throwable -> handleError(throwable))
                .onErrorReturn(throwable -> null);*/
    }
}
