import io.reactivex.schedulers.Schedulers;

/**
 * Created by Amandeep Singh Bagli on 10/06/17.
 */

public class MovieDetailPresenter {

    private final MovieRepository movieRepository;
    private final MovieDetailContract.View movieDetailView;
    private boolean mFirstLoad = true;

    public MovieDetailPresenter(MovieRepository movieRepository, MovieDetailContract.View movieDetailView) {

        this.movieRepository = movieRepository;
        this.movieDetailView = movieDetailView;
        movieDetailView.setPresenter(this);

    }


    public void start() {
        loadMovieDetail(false);
    }

    public void loadMovieDetail(boolean forceUpdate) {

        // Simplification for sample: a network reload will be forced on first load.
        loadMovieDetail(forceUpdate || mFirstLoad, true);
        mFirstLoad = false;
    }


    /**
     * @param forceUpdate   Pass in true to refresh the data in the {
