import io.dropwizard.testing.ResourceHelpers;
import org.junit.After;
import org.junit.Before;
import org.junit.ClassRule;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class IntegrationTest {
  private static final String TMP_FILE = createTempFile();
  private static final String CONFIG_PATH = ResourceHelpers.resourceFilePath("config.yml");

  @ClassRule
  public static final DropwizardAppRule<ServiceConfiguration> RULE =
          new DropwizardAppRule<ServiceConfiguration>(Service.class, CONFIG_PATH,
                  ConfigOverride.config("database.url", "jdbc:h2:" + TMP_FILE));

  private ImmutableList<ServiceDTO> serviceDTOS;

  @Before
  public void setup() {
    serviceDTOS = ImmutableList.of(
            new ServiceDTO(1L, "name1", "url1", "status1", "health1"),
            new ServiceDTO(2L, "name2", "
