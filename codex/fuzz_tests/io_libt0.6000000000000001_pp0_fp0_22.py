import io.realm.RealmObject;

public class User extends RealmObject {
    @PrimaryKey
    private String id;
    private String name;
    private String password;
    private String email;
    private String phone;
    private String address;
    private String image;
    private String token;

    public User() {
    }

    public User(String id, String name, String password, String email, String phone, String address, String image, String token) {
        this.id = id;
        this.name = name;
        this.password = password;
        this.email = email;
        this.phone = phone;
        this.address = address;
        this.image = image;
        this.token = token;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public
