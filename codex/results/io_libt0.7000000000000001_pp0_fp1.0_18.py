import io.github.cexj.declarser.kernel.parsers.Parser;
import io.github.cexj.declarser.kernel.parsers.ParserFactory;
import io.github.cexj.declarser.kernel.tryapi.Try;
import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class LocalDateTimeParserTest {

    /*
     * GIVEN a LocalDateTime parser
     *  AND a valid String representation
     *  AND a valid formatter
     * WHEN the parser is invoked
     * THEN it must return a success try
     *  AND the value contained must be the local date time representation of the string
     */
    @Test
    public void valid_string_representation_return_success_try() {
        // G
