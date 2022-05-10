import io.github.alexswilliams.serialisation.jackson.json.PersonDeserialiser;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.IOException;

class PersonDeserialiserTests {
    @Test
    void canDeserialise() throws IOException {
        final var classUnderTest = new PersonDeserialiser();

        final var json =
                "{" +
                        "\"name\":\"A Williams\"," +
                        "\"age\":19," +
                        "\"isAlive\":true" +
                "}";

        final var expected = new Person("A Williams", 19, true);

        final var actual = classUnderTest.readValue(json);

        Assertions.assertEquals(expected, actual);
    }
}
