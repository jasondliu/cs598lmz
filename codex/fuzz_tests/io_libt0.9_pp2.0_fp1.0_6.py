import io.realm.annotations.PrimaryKey;
import io.realm.annotations.RealmClass;

/**
 * Created by Hitesh on 4/9/2016.
 */
@RealmClass
public class ModelReadSync implements Serializable {

    @PrimaryKey
    int id;

    int newsId;
    String newsContent;
    byte[] newsImage;
    String newsTitle;
    String date;
    String time;


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getNewsId() {
        return newsId;
    }

    public void setNewsId(int newsId) {
        this.newsId = newsId;
    }

    public String getNewsContent() {
        return newsContent;
    }

    public void setNewsContent(String newsContent) {
        this.newsContent = newsContent;
    }

    public byte[] getNewsImage() {
        return newsImage;
    }

    public void setNews
