import io.github.dector.quotes.Quites
import io.github.dector.quotes.presentation.main.Screen

@Reducer
class MainReducer(private val quotes: Quites) {

    fun reduce(action: Action, state: State): State =
        when (action) {
            Action.Init -> initState
            is Action.BindApi -> bindApi(state, action.api)
            is Action.Error -> processError(state, action.throwable)
            Action.Refresh -> fetchQuotes(state)
            is Action.SelectQuote -> selectQuote(state, action.quote)
        }

    private val initState: State get() = State.Default(Screen.Listing)

    private fun bindApi(state: State, api: QuotesApi): State = when (state) {
        is State.Default -> state.copy(quotesApi = api)
        is State.Loading -> state.copy(quotesApi = api)
        is State.Error -> state.copy(quotesApi = api)
        is State.Details -> state.
