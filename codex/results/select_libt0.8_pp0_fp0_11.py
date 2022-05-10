import selectors.SelectorsTab;
import selectors.IDSelector;
import selectors.ClassSelector;
import selectors.ChildSelector;
import selectors.DescendantOrSelfSelector;
import selectors.DirectAdjacentSelector;
import selectors.ElementNameSelector;
import selectors.PseudoElementSelector;
import selectors.SubstringAttributeSelector;
import selectors.SuffixAttributeSelector;
import selectors.SubstringAfterSuffixAttributeSelector;
import selectors.UniversalSelector;

public class SelectorsTabTest {

    @Test
    public void testSelectorsTab() {
        SelectorsTab tab = SelectorsTab.getInstance();
        assertEquals("Selectors", tab.getTitle());
    }

    @Test
    public void testIDHash() {
        IDSelector selector = new IDSelector("hash");
        assertEquals("#hash", selector.toString());
    }

    @Test
    public void testIDPeriod() {
        IDSelector selector = new IDSelector("period");
        assert
