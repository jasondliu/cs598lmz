import io.reactivex.Single
import javax.inject.Inject

class GetRecentPlacesUseCase @Inject constructor(
    private val placeRepository: PlaceRepository
) {

    fun execute(): Single<List<Place>> {
        return placeRepository.getRecentPlaces()
    }
}
