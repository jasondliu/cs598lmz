import io.github.dunwu.spring.mvc.annotation.*;
+import io.github.dunwu.spring.mvc.service.UserService;
+
+@RestController
+@RequestMapping("/api/user/")
+public class UserController {
+
+    @Autowired
+    private UserService userService;
+
+    /**
+     * 更新用户信息
+     * @param user
+     * @return
+     */
+    @RequestMapping(value = "update", method = RequestMethod.PUT)
+    public Object update(@RequestBody User user) {
+        System.out.println(user);
+        System.out.println(user.getUserName());
+        return "OK";
+    }
+
+    /**
+     * 根据ID获取用户
+     * @param id
+     * @return
+     */
+    @RequestMapping(value = "{id}", method = RequestMethod
