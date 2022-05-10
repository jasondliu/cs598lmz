import io.reactivex.Single
import javax.inject.Inject

class GetAllMoviesUseCase @Inject constructor(private val movieRepository: MovieRepository){

    fun execute(): Single<List<Movie>> {
        return movieRepository.getAllMovies()
    }
}
