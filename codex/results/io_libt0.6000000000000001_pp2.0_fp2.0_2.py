import io.github.spharris.pvwatts.service.WeatherStationService;
import io.github.spharris.pvwatts.service.WeatherStationService.GetWeatherStationsResponse;
import io.github.spharris.pvwatts.service.WeatherStationService.GetWeatherStationsRequest;
import io.github.spharris.pvwatts.service.WeatherStationService.ListWeatherStationsRequest;
import java.util.Optional;
import javax.inject.Inject;
import javax.inject.Named;

/**
 * Implementation of {@link WeatherStationService}
 */
@Named
public final class GetWeatherStationsHandler implements
    Handler<GetWeatherStationsRequest, GetWeatherStationsResponse> {

  private final WeatherStationDao weatherStationDao;

  @Inject
  GetWeatherStationsHandler(WeatherStationDao weatherStationDao) {
    this.weatherStationDao = weatherStationDao;
  }

  @Override
  public GetWeatherStationsResponse handle(GetWeatherStationsRequest request
