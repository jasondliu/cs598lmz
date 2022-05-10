import io.github.morgaroth.base.{Model, ModelApi}
import io.github.morgaroth.base.mongo.DBAccess
import io.strongtyped.funcqrs.{CommandHandler, AggregateId, AggregateModule}
import org.joda.time.DateTime

// domain
case class Stock(id: StockId, title: String, description: String)

// commands
case class AddItem(id: StockId, title: String, description: String, tags: List[String] = List.empty)

// events
case class ItemAdded(id: StockId, title: String, description: String, tags: List[String])

// projections
case class StockItemView(title: String, description: String, tags: List[String])

// queries
case class FindStock(id: StockId)
case object StockList

// api
case class StockAPI(id: StockId, title: String, description: String, tags: List[String], created: DateTime) extends ModelApi[Stock]

class StockModule extends AggregateModule {

  val
