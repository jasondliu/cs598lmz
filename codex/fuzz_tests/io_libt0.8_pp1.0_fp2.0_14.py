import io.seal.swarmwear.lib.service.SignInService;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.runners.MockitoJUnitRunner;

import static org.mockito.Mockito.verify;

@RunWith(MockitoJUnitRunner.class)
public class GoogleApiConnectedReceiverTest {

    @Mock
    private FragmentActivity mFragmentActivity;

    @Mock
    private SignInService mSignInService;

    @Mock
    private Intent mIntent;

    private GoogleApiConnectedReceiver mGoogleApiConnectedReceiver;

    @Before
    public void setUp() {
        mGoogleApiConnectedReceiver = new GoogleApiConnectedReceiver(mFragmentActivity, mSignInService);
    }

    @Test
    public void testOnReceive() throws Exception {
        mGoogleApiConnectedReceiver.on
