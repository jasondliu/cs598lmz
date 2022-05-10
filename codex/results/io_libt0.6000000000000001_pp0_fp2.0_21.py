import io.reactivex.Single
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.koin.core.KoinComponent
import org.koin.core.inject

class FabricRepository : KoinComponent {
    private val fabricDao: FabricDao by inject()

    fun getFabric(): Single<List<Fabric>> {
        return fabricDao.getFabric()
    }

    fun getFabricById(id: Int): Single<Fabric> {
        return fabricDao.getFabricById(id)
    }

    suspend fun insertFabric(fabric: Fabric) =
        withContext(Dispatchers.IO) {
            fabricDao.insertFabric(fabric)
        }

    suspend fun deleteFabricById(id: Int) =
        withContext(Dispatchers.IO) {
            fabricDao.deleteFabricById(id)
        }

    suspend fun updateFabric(fabric: Fabric) =
        withContext(Dispatchers.IO) {
