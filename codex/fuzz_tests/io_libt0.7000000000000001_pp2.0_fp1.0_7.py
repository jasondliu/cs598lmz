import io.realm.RealmObject;
import io.realm.annotations.PrimaryKey;

public class CurrencyModel extends RealmObject implements Serializable{

    @PrimaryKey
    private String currencyCode;

    private String currencyName;

    private String currencySymbol;


    public CurrencyModel(){

    }

    public CurrencyModel(String currencyCode, String currencyName, String currencySymbol) {
        this.currencyCode = currencyCode;
        this.currencyName = currencyName;
        this.currencySymbol = currencySymbol;
    }

    public String getCurrencyCode() {
        return currencyCode;
    }

    public void setCurrencyCode(String currencyCode) {
        this.currencyCode = currencyCode;
    }

    public String getCurrencyName() {
        return currencyName;
    }

    public void setCurrencyName(String currencyName) {
        this.currencyName = currencyName;
    }

    public String getCurrencySymbol() {
        return currencySymbol;
    }

    public void setCurrencySymbol(String currencySymbol) {
