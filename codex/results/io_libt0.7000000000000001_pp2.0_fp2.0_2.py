import io.vavr.collection.List;
import io.vavr.collection.Stream;
import lombok.Getter;

public class ResultSetConverter<T> {

  private final Class<T> rootEntityClass;
  private final List<Class<?>> entityClasses;
  private final List<String> entityClassNames;
  private final List<String> columnNames;

  @Getter
  private final int rowCount;

  public ResultSetConverter(Class<T> rootEntityClass, List<Class<?>> entityClasses, List<String> columnNames, int rowCount) {
    this.rootEntityClass = rootEntityClass;
    this.entityClasses = entityClasses;
    this.entityClassNames = entityClasses.map(Class::getName);
    this.columnNames = columnNames;
    this.rowCount = rowCount;
  }

  public Stream<T> convert(ResultSet resultSet) {
    return Stream.range(0, rowCount).map(i -> {
      return convertSingleResultSet(resultSet);
    });

