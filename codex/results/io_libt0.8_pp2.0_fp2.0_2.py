import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;

/**
 * @ClassName: GlobalExceptionController
 * @Description: 全局异常处理
 * @author caiyang
 * @date 2019年1月22日 下午5:06:27
 * 
 */
@ControllerAdvice
@RestController
public class GlobalExceptionController {

	/**
	 * @Title: defaultErrorHandler
	 * @Description: 自定义异常处理
	 * @auther caiyang
	 * @date 2019年1月22日 下午5:06:36
	 * @param ex
	 * @param request
	 * @param response
	 * @return
	 * @throws Exception
	 * @return String
	 * 
	 */
	@ExceptionHandler(value = Exception.class)
	@ResponseBody
	@ApiOperation(value = "自定义异常
