import selection.QueryHandler;

public class SearchController extends HttpServlet {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private static final Logger logger = Logger.getLogger(SearchController.class);
	private QueryHandler queryHandler = new QueryHandler();
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession(true);
		// session.setMaxInactiveInterval(3000);
		//session.invalidate();
		PrintWriter out = response.getWriter();

		out.println("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " + "Transitional//EN\">\n" + "<HTML>\n" + "<HEAD><TITLE>"+ "Search" + "</TITLE>\n" + "</HEAD>\n" + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER
