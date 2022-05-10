import io.github.t3r1jj.pbmap.main.AppResources
import io.github.t3r1jj.pbmap.model.map.Coordinate
import io.github.t3r1jj.pbmap.testing.InstantTaskExecutorExtension
import io.github.t3r1jj.pbmap.view.map.MapView
import io.mockk.AwaitKt.await
import io.mockk.Runs
import io.mockk.every
import io.mockk.just
import io.mockk.mockk
import io.mockk.spyk
import io.mockk.verify
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.extension.ExtendWith
import java.util.concurrent.ExecutionException
import java.util.concurrent.TimeUnit

@ExtendWith(InstantTaskExecutorExtension::class)
internal class PBMMapViewControllerTest {

    private lateinit var
