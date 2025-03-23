package com.lcontrol;

import io.github.bonigarcia.wdm.WebDriverManager;
import io.qameta.allure.*;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@Epic("Web Application Testing")
@Feature("S3 Static Website Tests")
public class WebSiteTest {

    private WebDriver driver;
    private static final String BASE_URL = "http://lcontrol-test-site.s3-website.eu-north-1.amazonaws.com";
    private static final String SCREENSHOT_DIR = "screenshots";
    private String fileName;

    /**
     * Sets up the Chrome WebDriver with headless mode and creates the screenshot directory if it doesn't exist.
     */
    @BeforeEach
    public void setUp() {
        WebDriverManager.chromedriver().setup();
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless=new"); // Headless Mode For CI/CD
        options.addArguments("--no-sandbox");   // Linux CI
        options.addArguments("--disable-dev-shm-usage"); // Prevent memory issues in CI
        driver = new ChromeDriver(options);

        File dir = new File(SCREENSHOT_DIR);
        if (!dir.exists()) {
            dir.mkdirs();
        }else{
            System.out.println("SCREENSHOT_DIR Already Exist");
        }
    }

    @Test
    @Story("Verify Homepage and Interactions")
    @Description("Test the homepage load, navigation links, and form submission")
    public void testHomepage() throws Exception {
        // 1. check HomePage Loading
        driver.get(BASE_URL);
        Thread.sleep(2000);
        String pageSource = driver.getPageSource();
        assertTrue(pageSource.contains("Welcome to My Test Site"), "Homepage failed to load");
        takeScreenshot("homepage_loaded.png");
        System.out.println("Homepage loaded successfully");

        // 2. Check Navigation links
        List<WebElement> links = driver.findElements(By.tagName("a"));
        assertEquals(2, links.size(), "Expected 2 navigation links, found " + links.size());
        for (WebElement link : links) {
            String linkText = link.getText();
            assertTrue(linkText.equals("Home") || linkText.equals("Contact"),
                    "Unexpected link text: " + linkText);
        }
        WebElement contactLink = driver.findElement(By.xpath("//a[text()='Contact']"));
        assertTrue(contactLink.getAttribute("href").contains("mailto:"),
                "Contact link does not contain an email");
        takeScreenshot("navigation_links.png");
        System.out.println("Navigation links verified");

        // 3.Check Form Sent
        WebElement usernameField = driver.findElement(By.name("username"));
        WebElement submitButton = driver.findElement(By.xpath("//input[@type='submit']"));
        usernameField.sendKeys("s3-test-user");
        takeScreenshot("form_filled.png");
        submitButton.click();
        Thread.sleep(1000);
        takeScreenshot("form_submitted.png");
        System.out.println("Form submission completed");
    }

    /**
     * Captures a screenshot from the browser and saves it as a PNG file.
     *
     * @param fileName the name of the file to save the screenshot (e.g., "test1.png")
     * @throws Exception if the screenshot capture or file saving operation fails
     */
    @Attachment(value = "Screenshot", type = "image/png")
    public byte[] takeScreenshot(String fileName) throws Exception {
        TakesScreenshot screenshot = (TakesScreenshot) driver;
        File srcFile = screenshot.getScreenshotAs(OutputType.FILE);
        Path destPath = Paths.get(SCREENSHOT_DIR, fileName);
        Files.copy(srcFile.toPath(), destPath, StandardCopyOption.REPLACE_EXISTING);
        System.out.println("Screenshot saved: " + destPath);
        return screenshot.getScreenshotAs(OutputType.BYTES);

    }

    @AfterEach
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}