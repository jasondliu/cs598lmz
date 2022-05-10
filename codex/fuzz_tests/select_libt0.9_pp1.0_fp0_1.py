import selectmyride.common.helper;
import java.sql.SQLException;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 *
 * @author kapil
 */
public class userpurchase extends BaseClass {

    public userpurchase(HttpServletRequest request, HttpServletResponse response) throws Exception {
        super(request, response);
    }

    public void usercarinfo() throws Exception {
        try {
            JSONArray data = service.fetch("select car_id,car_name,cc,fuel_type,car_model_year,img1,car_price,dealer_id,remarks from cars where user_id=" + user_id);
            helper.DataToJson(data, out);
        } catch (Exception e) {
            helper.PrintStackTrace(e, out);
        } finally {
            service.close();
        }

    }

    public void carpurchaserequest() throws Exception {
        try {
            String car_id = helper.getParam("car_id
