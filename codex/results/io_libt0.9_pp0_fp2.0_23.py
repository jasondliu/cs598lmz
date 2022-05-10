import io.confluent.ksql.test.util.TestMethodUtil;
import java.lang.reflect.Method;
import org.junit.runners.model.InitializationError;
import org.junit.runners.model.Statement;

public class IntegrationTestRule extends KsqlRule {

  /**
   * This test runner requires that tests be annotated with {@link KsqlTestUtil}.
   * @throws InitializationError
   */
  public IntegrationTestRule() throws InitializationError {
    super(IntegrationTestRule.class);
  }

  @Override
  protected Statement methodInvoker(final FrameworkMethod method, final Object test) {
    if (method.getAnnotation(KsqlTestUtil.class) == null) {
      throw new IllegalArgumentException("Method " + method.getName()
          + " is not annotated with " + KsqlTestUtil.class.getSimpleName());
    }

    return super.methodInvoker(method, test);
  }

  @Override
  protected Statement withAfters(
      final FrameworkMethod method,
      final Object
