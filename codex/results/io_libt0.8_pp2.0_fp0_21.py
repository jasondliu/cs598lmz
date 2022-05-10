import io.yogh.zeroconf.shared.domain.Pair;

import com.google.gwt.json.client.JSONObject;
import com.google.gwt.json.client.JSONValue;

public class PlaceDeserializer implements Deserializer<Place> {
  private static final String LAT_KEY = "lat";
  private static final String LON_KEY = "lon";

  @Override
  public Place deserialize(final JSONObject object) {
    final JSONValue latValue = object.get(LAT_KEY);
    final JSONValue lonValue = object.get(LON_KEY);

    if (latValue == null || lonValue == null) {
      return null;
    }

    final double lat = latValue.isNumber().doubleValue();
    final double lon = lonValue.isNumber().doubleValue();

    return new Place(new Pair<Double, Double>(lat, lon));
  }
}
