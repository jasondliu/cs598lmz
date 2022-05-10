import io.realm.RealmResults;
import io.realm.Sort;
import retrofit.Call;
import retrofit.Callback;
import retrofit.Response;
import retrofit.Retrofit;

/**
 * Created by Juan on 12/05/2017.
 */

public class DBManager {
    private Realm realm = null;
    private Context context = null;
    private Call<ArrayList<Team>> call = null;

    public DBManager(Context context){
        this.context = context;
    }

    public void retrieveTeams() {
        if (realm == null) realm = Realm.getDefaultInstance();
        call = F1Api.getInstance(context).listTeam();

        call.enqueue(new Callback<ArrayList<Team>>() {
            @Override
            public void onResponse(Response<ArrayList<Team>> response, Retrofit retrofit) {
                ArrayList<Team> teams = response.body();

                realm.beginTransaction();
                realm.copyToRealmOrUpdate(teams);
                realm.commitTransaction();

                loadChampionList
