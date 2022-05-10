import io.swagger.annotations.ApiModelProperty;

public class User {
	
	@ApiModelProperty(hidden = true)
	private int id;
	
	@ApiModelProperty(required = true)
	private String name;
	@ApiModelProperty(required = true)
	private String email;
	@ApiModelProperty(required = true)
	private String password;
	@ApiModelProperty(required = true)
	private String username;
	
	public User() {
		
	}
	
	public User(String name, String email, String password, String username) {
		super();
		this.name = name;
		this.email = email;
		this.password = password;
		this.username = username;
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName
