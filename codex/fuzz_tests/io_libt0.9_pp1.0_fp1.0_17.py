import io.realm.annotations.Required;

/**
 * Created by Maikel on 30-08-2015.
 */

@JsonIgnoreProperties(ignoreUnknown = true)
public class Image {

    @JsonProperty("#text")
    @PrimaryKey
    private String text;
    @Required
    private String size;

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
}
