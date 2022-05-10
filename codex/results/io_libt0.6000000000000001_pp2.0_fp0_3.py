import io.realm.RealmObject;
import io.realm.annotations.PrimaryKey;

/**
 * Created by Lukas on 12/05/2017.
 */

public class RealmUser extends RealmObject {

    @PrimaryKey
    private String id;

    private String name;

    private String email;

    private String password;

    private String photo;

    private String token;

    private boolean gps;

    private boolean email_notification;

    private boolean push_notification;

    private int type;

    private int gender;

    private int age;

    private int height;

    private int weight;

    private double longitude;

    private double latitude;

    private String device;

    private String created_at;

    private String updated_at;

    public RealmUser() {
    }

    public RealmUser(User user) {
        this.id = user.getId();
        this.name = user.getName();
        this.email = user.getEmail();
        this.password = user.getPassword();
        this.photo = user.getPhoto();
