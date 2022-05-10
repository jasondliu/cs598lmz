import io.getquill.iteratee.Enumerator
import io.getquill.naming.SnakeCase
import io.getquill.sources.sql.idiom.PostgresDialect
import io.getquill.sources.sql.idiom.SqlIdiom
import io.getquill.sources.SourceConfig

trait H2JdbcContext[Dialect <: SqlIdiom, Naming <: NamingStrategy]
  extends JdbcContext[Dialect, Naming]
  with H2JdbcSource
  with Decoders
  with Encoders {

  def probe(sql: String) =
    this.execute(sql)
}

trait H2JdbcSource extends JdbcSource[PostgresDialect, SnakeCase] {

  override protected def dataSource: DataSource with Closeable =
    new ComboPooledDataSource()

  def close() =
    dataSource.asInstanceOf[ComboPooledDataSource].close
}

object H2JdbcContext {

  def apply[N <: N
