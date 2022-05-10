import io.github.mandar2812.daedalus.turing.{DTM, TMTape}
import org.scalatest.{FlatSpec, Matchers}

/**
  * @author mandar2812 on 21/4/16.
  */
class TuringSpec extends FlatSpec with Matchers {
  "A DTM" should "accept a string of a's and b's" in {
    val tm = new DTM(
      Map(
        0 -> Map(
          'a' -> (1, 'a', R),
          'b' -> (2, 'b', R)
        ),
        1 -> Map(
          'a' -> (1, 'a', R),
          'b' -> (0, 'b', L)
        ),
        2 -> Map(
          'a' -> (2, 'a', R),
          'b' -> (0, 'b', L)
        )
      ),
      Set(0),
      1,
      Set(0)
    )

    val tape = new TMTape(List('a',
