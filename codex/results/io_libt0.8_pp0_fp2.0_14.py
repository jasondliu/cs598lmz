import io.github.adaok.moreorless.core.GameRepository
import io.github.adaok.moreorless.core.model.Game
import io.github.adaok.moreorless.core.model.GameState

class SharedPreferencesGameRepository(private val sharedPrefs: SharedPreferences) : GameRepository {

    override fun findGameById(id: String): Game? {
        return sharedPrefs.getString(id, null)?.let { json ->
            Gson().fromJson(json, Game::class.java)
        }
    }

    override fun insertGame(game: Game) {
        val editor = sharedPrefs.edit()
        val json = Gson().toJson(game)
        editor.putString(game.id, json)
        editor.apply()
    }

    override fun updateGame(game: Game) {
        val editor = sharedPrefs.edit()
        val json = Gson().toJson(game)
        editor.putString(game.id, json)
        editor.apply()
    }
}
