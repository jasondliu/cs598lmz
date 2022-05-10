import io.vavr.collection.Seq;
import io.vavr.collection.Set;
import io.vavr.collection.Traversable;
import lombok.NonNull;
import lombok.Value;
import lombok.experimental.Wither;
import org.apache.commons.lang3.Validate;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.function.Consumer;
import java.util.function.Predicate;

@Value
@Wither
public class MatchDate {

    @NonNull
    LocalDate date;
    @NonNull
    Set<String> wjhgHome;
    @NonNull
    Set<String> wjhgAway;

    public static MatchDate ofWjhg(@NonNull final WjhgMatchDate wjhg) {
        final Set<String> home = wjhg.getHomeTeams().map(Team::getName);
        final Set<String> away = wjhg.getA
