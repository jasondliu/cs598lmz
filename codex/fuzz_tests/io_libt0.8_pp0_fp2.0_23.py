import io.freshdroid.mymonzo.models.Transaction
import io.reactivex.Observable
import kotlinx.android.parcel.Parcelize

@Parcelize
data class TransactionFeedViewState(
    val success: Boolean = false,
    val loading: Boolean = true,
    val transactions: List<Transaction> = listOf()
) : ViewState

data class TransactionFeedViewStateSingle(
    val success: Boolean = false,
    val loading: Boolean = true,
    val transactions: List<Transaction> = listOf()
) : SingleViewState<Transactio
