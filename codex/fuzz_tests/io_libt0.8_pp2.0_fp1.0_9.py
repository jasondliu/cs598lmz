import io.reactivex.schedulers.Schedulers;

public class RxJavaActivity extends AppCompatActivity {

    public List<String> data = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_rx_java);

        Call<MovieEntity> call = RetrofitHelper.getInstance().getApiService(ApiService.class).getTopMovie(0, 10);
        call.enqueue(new Callback<MovieEntity>() {
            @Override
            public void onResponse(Call<MovieEntity> call, Response<MovieEntity> response) {
                data.clear();
                for (MovieEntity.SubjectsBean subjectsBean : response.body().getSubjects()) {
                    data.add(subjectsBean.getTitle());
                }
            }

            @Override
            public void onFailure(Call<MovieEntity> call, Throwable t) {

            }
        });

        Flowable.create(new FlowableOn
