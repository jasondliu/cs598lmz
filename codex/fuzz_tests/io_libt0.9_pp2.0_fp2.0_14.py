import io.dcloud.HBuilder.SVG.SVGActivity;
import io.dcloud.HBuilder.SVG.SVGParse;
import io.dcloud.HBuilder.SVG.SVGParser;
import io.dcloud.HBuilder.SVG.SVGUtil;
import io.dcloud.HBuilder.SVG.ThreadPool.ThreadPool;
import io.dcloud.HBuilder.SVG.ThreadPool.ThreadPool.JobContext;
import io.dcloud.HBuilder.SVG.Util;

/**
 * widget view
 *
 * @author haoge
 *
 */
public class WXSVGView extends View implements ISVGView, SVGParse.ParseComplete {

	private static final String TAG = "WXSVGView";

	private SVGParser mParser;
	private SVGParse mParseRender;
	private SVGActivity mActivity;
	private boolean mPaused = false;

	private ViewGroup mParent;
	private Matrix matrix = new Matrix();
	private Bitmap winmakeBitmap;
	public static int width,
