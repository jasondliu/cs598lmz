import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._
import scala.concurrent.forkjoin.ThreadLocalRandom
import scalaj.http.{Http, HttpOptions}
import java.net.URLEncoder

//import java.util.concurrent.TimeUnit
//import scala.collection.JavaConverters._
//import java.util.{Map => JMap}
//import io.gatling.core.Predef._
//import io.gatling.http.Predef._
//import scala.concurrent.duration._
//import scala.concurrent.forkjoin.ThreadLocalRandom
//import io.gatling.core.feeder._
//import java.net.URLEncoder
//import io.gatling.core.ConfigKeys
//import io.gatling.commons.validation._
//import scala.util.Random

class BasicSimulation extends Simulation {

  val httpConf = http
    .baseURL("https://tf-dev-citizen-api.dev.az
