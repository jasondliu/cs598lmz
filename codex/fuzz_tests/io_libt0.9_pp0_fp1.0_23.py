import io.reactivex.Completable
import java.util.*
import javax.inject.Inject

/**
 * Use Case to save a new Game to the database
 */
class SaveGames @Inject constructor(private val gamesDao: GamesDao) {

    fun execute(games: List<Game>): Completable {
        return gamesDao.insert(games)
    }
}
