import selector.Selector;
import selector.Selector.update_option;
import util.Log;
import util.Util;

public class UtilTest {

	@Test
	public void test() {
		fail("Not yet implemented");
	}
	
	
	@Test
	public void test_set_file_content_to_file() {
		String file = "d:\\tmp\\aaa.txt";
		File f = new File(file);
		if (f.exists()) {
			f.delete();
		}
		Util.set_file_content_to_file("123456789", file);
		String content = Util.get_file_content_from_file(file);
		assertEquals("123456789", content);
	}
	
	@Test
	public void test_get_file_content_from_file() {
		String file = "d:\\tmp\\aaa.txt";
		File f = new File(file);
		if (f.exists())
