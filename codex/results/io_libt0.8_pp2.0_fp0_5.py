import io.realm.RealmObject
import io.realm.annotations.PrimaryKey
import io.realm.annotations.RealmClass

@RealmClass
open class CurrencyDataModel(
    @PrimaryKey var id: Int = 0,
    var currencyCode: String = "",
    var currencyName: String = ""
) : RealmObject()
