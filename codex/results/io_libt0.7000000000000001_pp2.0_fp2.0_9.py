import io.reactivex.Single
import javax.inject.Inject

class LocalImageDataSource @Inject constructor(
    private val imageDao: ImageDao
) : ImageDataSource {

    override fun isCached(): Single<Boolean> {
        return imageDao.getImages().isEmpty.map { !it }
    }

    override fun getImages(): Single<List<Image>> {
        return imageDao.getImages()
    }

    override fun saveImages(image: List<Image>) {
        imageDao.insertAll(image)
    }

    override fun clearImages() {
        imageDao.deleteAll()
    }
}
