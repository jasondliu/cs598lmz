import io.github.binaryfoo.bitwise.ByteArrayView;

import static io.github.binaryfoo.bitwise.BitwiseView.hex;
import static org.junit.Assert.assertEquals;

public class TVRTest {
    private TVR tvr;


    @Test
    public void isTerminalRiskAnalysisFlags() throws Exception {
        tvr = new TVR(hex("000000000000000000000000000000"));
        assertEquals(Arrays.asList(), tvr.getTerminalRiskAnalysisFlags());

        tvr = new TVR(hex("F000000000000000FF0000000000000"));
        assertEquals(Arrays.asList("Offline data authentication was performed",
                "Issuer authentication was performed",
                "Terminal risk management was performed",
                "New card",
                "Cardholder verification was not successful",
                "Unrecognised CVM",
                "PIN Try Limit exceeded",
                "CVM Failure limit exceeded",
                "Default TDOL used",
                "Issuer authentication failed"), tvr.getTerminalRiskAnalysisFlags());
    }

    @Test
