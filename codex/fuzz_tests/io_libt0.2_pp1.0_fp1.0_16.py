import io.reactivex.schedulers.Schedulers;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    private static final String BASE_URL = "https://api.github.com/";

    private static final String USER_NAME = "jakewharton";

    private static final String REPO_NAME = "butterknife";

    private static final String REPO_URL = BASE_URL + "repos/" + USER_NAME + "/" + REPO_NAME;

    private static final String REPO_URL_WITH_AUTH = BASE_URL + "repos/" + USER_NAME + "/" + REPO_NAME + "/contributors";

    private static final String REPO_URL_WITH_AUTH_AND_PARAMS = BASE_URL + "repos/" + USER_NAME + "/" + REPO_NAME + "/contributors?page=1&per_page=10";

    private static final String REPO_URL_WITH_AUTH_AND_PARAMS_AND_HEADERS = BASE
