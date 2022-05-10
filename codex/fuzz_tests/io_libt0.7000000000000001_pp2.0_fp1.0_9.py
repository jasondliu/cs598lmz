import io.janstenpickle.trace4cats.model.SpanKind
import io.janstenpickle.trace4cats.model.TraceHeaders.{ClientParentSpanId, SpanId}
import io.janstenpickle.trace4cats.kernel.SpanSampler
import io.janstenpickle.trace4cats.model.{AttributeValue, SpanKind, TraceHeaders}
import io.janstenpickle.trace4cats.model.AttributeValue.StringValue
import io.janstenpickle.trace4cats.test.ArbitraryInstances
import io.janstenpickle.trace4cats.test.ArbitraryInstances.{arbitrarySpanId, arbitrarySpanName}
import org.scalacheck.{Arbitrary, Gen}
import org.scalacheck.Arbitrary.{arbitrary => arb}
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers
import org.scalatestplus.scalacheck.ScalaCheckDrivenProperty
