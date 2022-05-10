import io.vavr.Tuple;
import io.vavr.control.Option;

import java.util.Arrays;
import java.util.List;
import java.util.function.BiPredicate;
import java.util.function.DoubleFunction;

/**
 * Class to represent 2 element vector.
 */
@ToString
@Slf4j
@Getter
public class Vector2d {
    public static final Vector2d ORIGIN = new Vector2d(0, 0);
    public static final Vector2d X_UNIT = new Vector2d(1, 0);
    public static final Vector2d Y_UNIT = new Vector2d(0, 1);
    public static final Vector2d X_NEGATIVE_UNIT = new Vector2d(-1, 0);
    public static final Vector2d Y_NEGATIVE_UNIT = new Vector2d(0, -1);

    private final double x;
    private final double y;

    public Vector2d(final double scalar) {
        this(scalar, scalar);
    }


