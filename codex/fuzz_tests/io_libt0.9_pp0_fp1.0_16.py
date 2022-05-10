import ioZhang.springboot.springbootweb.controller.HelloWorldController;
+
+@RunWith(SpringRunner.class)   // 底层用junit驱动
+@WebMvcTest(controllers = HelloWorldController.class)   // 只测试HelloWorldController
+public class SampleControllerTest {
+    @Autowired
+    private MockMvc mvc;    // 模拟mvc，用来发送http请求来调试
+
+    @Test
+    public void testHello() throws Exception {
+        // mvc.perform执行一个请求，andExpect添加验证断言
+        mvc.perform(MockMvcRequestBuilders.get("/hello").accept(MediaType.APPLICATION_JSON))
+                .andExpect(status().isOk())   // 验证结果
