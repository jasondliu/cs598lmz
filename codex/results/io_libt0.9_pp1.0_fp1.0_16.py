import io.appium.java_client.service.local.flags.GeneralServerFlag;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class AppiumService {
    protected IOSDriver<AppiumWebElement> driver = null;
    protected ChromeDriver driverChrome = null;
    private String pathToApp = "iOS/CeedTest.app";

    protected String app = null;
    private String device = "emulator";
    protected String os = "iOS";
    private String deviceVersion = "12.2";
    protected String browser = "Safari";
    private String deviceName = "iPhone XR";
    private int timeOutInSecond
