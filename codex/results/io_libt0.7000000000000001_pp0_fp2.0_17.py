import io.reactivex.schedulers.Schedulers;

import static com.example.android.movieapp.utils.Constants.API_KEY;

public class MovieRepository {

    private static final String TAG = MovieRepository.class.getSimpleName();
    private static MovieRepository instance;
    private MovieApiService movieApiService;


    public static MovieRepository getInstance() {
        if (instance == null) {
            instance = new MovieRepository();
        }
        return instance;
    }

    private MovieRepository() {
        movieApiService = MovieApiClient.getClient();
    }

    public LiveData<PagedList<Movie>> getPopularMovies(Activity activity) {
        LiveData<PagedList<Movie>> popularMoviesLiveData = new LiveData<PagedList<Movie>>() {
            @Override
            protected void onActive() {
                super.onActive();
                popularMoviesLiveData = new LivePagedListBuilder<>(
                        MovieDatabase.getInstance(activity).movieDao().getPopularM
