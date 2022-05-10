import mmapi.xmm.ResultSet;
import mmapi.xmm.types.Payload;

public class AnnotationCollection {
	
	private String name;
	private String colour;
	private String description;
	private String parent;
	
	private PayloadCollection payloads;
	//unused private ResultSet rs;
	
	public AnnotationCollection(String n) {
		name = n;
		payloads = new PayloadCollection();
	}
	
	public AnnotationCollection(String n, String c, String p) {
		name = n;
		colour = c;
		parent = p;
		payloads = new PayloadCollection();
	}
	
	
	public void setName(String n) {
		name = n;
	}
	
	public String getName() {
		return name;
	}
	
	public void setParent(String p) {
		parent = p;
	}
	
	public String getParent() {
		return parent;
	}
	
	public void
