import io.github.serpro69.kfaker.Faker
import io.github.serpro69.kfaker.provider.Address
import io.github.serpro69.kfaker.provider.Lorem
import io.github.serpro69.kfaker.provider.Name
import io.github.serpro69.kfaker.provider.unique.LocalUniqueDataProvider
import io.github.serpro69.kfaker.provider.unique.UniqueProviderDelegate

/**
 * [FakeDataProvider] implementation for [CategoryName.UNIQUE] category.
 */
@Suppress("unused")
class Unique internal constructor(fakerService: FakerService) : AbstractFakeDataProvider<Unique>(fakerService) {
    override val categoryName = CategoryName.UNIQUE
    override val localUniqueDataProvider = LocalUniqueDataProvider()
    override val unique by UniqueProviderDelegate(localUniqueDataProvider)

    fun avatars() = resolve("avatars")
    fun uuids() = resolve("uuids")
    fun passwords() = resolve("passwords")
    fun
