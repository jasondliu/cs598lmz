import io.learn.movieinfoservice.models.Movie;

@Service
public class MovieInfoService {
	
	@Autowired
	RestTemplate restTemplate;
	
	public Movie getMovieInfo(String movieId) {
		MovieSummary movieSummary = restTemplate.getForObject("https://api.themoviedb.org/3/movie/" + movieId
				+ "?api_key=a02c8d659987c45b5f049e56ea41f121", MovieSummary.class);
		
		return new Movie(movieId, movieSummary.getOriginal_title(), movieSummary.getOverview());
	}

}
