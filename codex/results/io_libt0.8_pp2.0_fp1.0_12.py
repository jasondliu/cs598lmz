import io.swagger.models.auth.In;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import javax.naming.directory.SearchControls;
import javax.servlet.http.HttpServletRequest;
import javax.validation.constraints.Null;
import java.lang.reflect.Array;
import java.util.*;

/**
 * Created by yuxin on 2017/9/11.
 */
@Controller
@EnableAutoConfiguration
@RequestMapping("/")
public class IndexController {
    @Autowired
    private InfoService infoService;

    @Autowired
    private FilesService filesService;

    @Autowired
    private UserService userService;

    @RequestMapping("
