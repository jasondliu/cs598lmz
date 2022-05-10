import io.reactivex.disposables.Disposable;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";
    private static final String BASE_URL = "https://api.github.com/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //create retrofit instance
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                .build();

        //get service and call object for the request
        GitHubService gitHubService = retrofit.create(GitHubService.class);
        Call<List<GitHubRepo>> call = gitHubService.reposForUser("fs-opensource");

        //asynchronous call
        call.enqueue(new Callback<List<GitHubRepo
