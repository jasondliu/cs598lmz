import io.circe.generic.auto._
import io.circe.parser.parse
import org.scalatest.{FlatSpec, Matchers}

class HttpJsonClientTest extends FlatSpec with Matchers {

  val client = new HttpJsonClient()

  it should "get json" in {
    val json = client.get(s"https://httpbin.org/get")
    assert(json.nonEmpty)
  }

  it should "post json" in {
    val data = Map("hello" -> "world")
    val json = client.post(s"https://httpbin.org/post", data)
    assert(json.nonEmpty)
    val result = parse(json).flatMap(_.hcursor.downField("form").downField("hello").as[String])
    assert(result.right.get == "world")
  }

}
