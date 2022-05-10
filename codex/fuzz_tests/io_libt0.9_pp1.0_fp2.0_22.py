import io.realm.Realm;


public class RealmHelper {

    Realm realm;

    //constructure
    public RealmHelper(Realm realm) {
        this.realm = realm;
    }


    //save
    public void save(final Note notes) {
        realm.executeTransaction(new Realm.Transaction() {
            @Override
            public void execute(Realm realm) {
                if (realm != null) {
                    Note mNote = realm.copyToRealm(notes);
                }
            }
        });
    }

    //select
    public List<Note> select() {
        RealmResults<Note> mNotes = realm.where(Note.class).findAll();
        return mNotes;
    }

    //update
    public void update(final String title, final String description, final int id) {
        realm.executeTransactionAsync(new Realm.Transaction() {
            @Override
            public void execute(Realm realm) {
                Note mNote = realm.where(Note.class)
                        .equalTo("id", id)
                        .findFirst();

