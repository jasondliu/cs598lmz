import io.github.kazuki_aruga.text_analyzer.entity.DocInfo;

/**
 * テキスト解析処理のインタフェース。
 *
 * @author kazuki
 */
public interface Analyzer {

	/**
	 * 文書情報を取得する。
	 *
	 * @param text
	 *            文書
	 * @return 文書情報
	 */
	DocInfo getDocInfo(String text);
}
