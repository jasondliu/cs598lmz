import io.realm.Realm
import io.realm.RealmResults
import io.realm.Sort
import io.realm.annotations.RealmModule
import ru.terrakok.cicerone.Navigator
import ru.terrakok.cicerone.Router
import ru.terrakok.cicerone.android.support.SupportAppScreen
import ru.terrakok.cicerone.commands.Back
import ru.terrakok.cicerone.commands.Command
import ru.terrakok.cicerone.commands.Forward
import java.util.*

/**
 * Created by text2 on 12.03.2018.
 */
open class AppViewModel() : ViewModel() {

    var database = DataBase()

    var router = Router()

    var navigator = Navigator {
        when (it) {
            is Forward -> router.navigateTo(it)
            is Back -> router.exit()
        }
    }

    fun init() {}

    override fun onCleared() {
        super.onCleared()
    }
}
