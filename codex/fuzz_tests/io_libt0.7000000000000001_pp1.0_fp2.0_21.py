import io.realm.Realm;
import io.realm.RealmResults;
import io.realm.Sort;
import io.realm.exceptions.RealmException;

/**
 * <p>Title:${type_inName}<p/>
 * <p>Description:<p/>
 * <p>Company: </p>
 *
 * @author litao
 * @mail llsmpsvn@gmail.com
 * @date on 2016/12/16
 */

public class RealmHelper implements DBHelper {

    public static final String DB_NAME = "myRealm.realm";

    private Realm mRealm;

    public RealmHelper(Context context) {
        Realm.init(context);
        RealmConfiguration realmConfiguration = new RealmConfiguration.Builder().name(DB_NAME).build();
        Realm.setDefaultConfiguration(realmConfiguration);
        mRealm = Realm.getDefaultInstance();
    }


    @Override
    public void insertNewsId(int id) {
        NewsId newsId = new NewsId();
        newsId.setId(id);

