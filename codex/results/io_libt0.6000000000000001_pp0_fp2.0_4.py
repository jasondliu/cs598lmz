import io.github.morgaroth.telegram.bot.bots.MorgarothBot
import io.github.morgaroth.telegram.bot.core.api.models.Update
import io.github.morgaroth.telegram.bot.core.engine.Core
import io.github.morgaroth.telegram.bot.core.engine.newengine.{NewUpdatesListener, NewUpdatesPolling}
import io.github.morgaroth.utils.mongodb.MongoDBLayer
import org.joda.time.DateTime

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future
import scala.util.{Failure, Success}

/**
  * Created by mateusz on 27.09.16.
  */
object Main extends App {

  MongoDBLayer.init()

  val token = MorgarothBot.token
  val bot = MorgarothBot.newBot(token)

  val engine = new NewUpdatesPolling with NewUpdatesListener {
    override def token
