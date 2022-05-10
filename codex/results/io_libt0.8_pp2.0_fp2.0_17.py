import io.github.cruisoring.oops.Asserts;
import io.github.cruisoring.repository.Repository;
import io.github.cruisoring.utility.ArrayHelper;
import io.github.cruisoring.utility.StringHelper;
import org.junit.Test;

import static io.github.cruisoring.Asserts.*;
import static io.github.cruisoring.Logger.Level.*;
import static io.github.cruisoring.utility.StringHelper.asString;

public class RepositoryTests {
    private static Repository<Integer, String> repository = Repository.ofKeyLists(Tuple.create("a", "b", "c", "d", "e"));

    static {
        repository.setLogger(Logger.getLogger(Repository.class));
    }

    @Test
    public void testRepositoryAddUpdate() {
        Logger.setLevel(Repository.class, TRACE);
        repository.addEntry(1, "1");
        assertAllTrue(repository.
