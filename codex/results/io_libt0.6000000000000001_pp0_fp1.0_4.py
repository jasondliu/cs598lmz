import io.reactivex.Single
import org.joda.time.DateTime
import org.joda.time.Duration
import org.joda.time.format.DateTimeFormat
import java.text.SimpleDateFormat
import java.util.*

class SearchPresenter(val view: SearchContract.View, val model: SearchContract.Model) : SearchContract.Presenter {

    init {
        view.presenter = this
    }

    override fun start() {
        view.setUpView()
        view.showLoading()
        model.getCities()
            .subscribeWith(object : DisposableSingleObserver<CitiesResponse>() {

                override fun onSuccess(response: CitiesResponse) {
                    view.hideLoading()
                    val cities = response.location_suggestions
                    if (cities.isNotEmpty()) {
                        view.showCities(cities)
                    } else {
                        view.showEmpty()
                    }
                }

                override fun onError(e: Throwable) {
                    view.hideLoading()
                    view.showError(e.local
