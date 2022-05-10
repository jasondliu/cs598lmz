import io.kotest.factory.Factory
import io.kotest.factory.FactoryConfigurationException
import io.kotest.factory.every
import io.kotest.factory.forAll
import io.kotest.factory.generator.fakerContext
import io.kotest.matchers.shouldBe
import io.kotest.matchers.string.startWith

@Suppress("unused")
class LambdaFactoryTest {

   @Test
   fun `should create unique instances each time`() {

      val list: List<String> = LambdaFactory.sample(N) { fakerContext.faker.name.name() }
      list shouldBe every { !isEmpty() && size == N }
      list shouldBe every { first() != last() }
   }

   @Test
   fun `should repeat instances`() {
      val list: List<String> = LambdaFactory.sample(N) { "same string" }
      list shouldBe every { this[0] == first() && this[0] == last() }
   }

  
