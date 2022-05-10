import io.intino.academy.content.DataCategory;
import io.intino.academy.files.File;
import io.intino.academy.files.NewFile;
import io.intino.academy.files.ResultFile;
import org.mapdb.DB;
import org.mapdb.DBMaker;

import java.io.FileNotFoundException;
import java.util.*;

import static java.util.stream.Collectors.toList;
import static java.util.stream.Collectors.toSet;

public class MapDbPersistor implements ContentRetriever, ContentPersistor {

    private final Map<String, DataCategory> dataCategoriesMap = new HashMap<String, DataCategory>() {{
        put("ARTICLE", DataCategory.ARTICLE);
        put("MOVIE", DataCategory.MOVIE);
    }};

    private final DB cache = DBMaker.fileDB("intino.db").fileMmapEnable().make();
    private final Cache<String, String> dataCategoryCache;
    private final Cache<Integer, Data
