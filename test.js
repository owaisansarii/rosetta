const { Builder, Browser, By, Key, until } = require("selenium-webdriver");

(async function example() {
  let driver = await new Builder().forBrowser(Browser.CHROME).build();
  try {
    await driver.get("https://login.rosettastone.com/#/login");
    // await driver.findElement(By.name("q")).sendKeys("webdriver", Key.RETURN);
    // await driver.wait(until.titleIs("webdriver - Google Search"), 4000);
    // data-qa = "Email" put email here
    await driver
      .findElement(By.css("input[data-qa='Email']"))
      .sendKeys("neelam30rawat@gmail.com");
    await driver
      .findElement(By.css("input[data-qa='Password']"))
      .sendKeys("rosetta@1234");
    setTimeout(() => {
      driver.findElement(By.css("div[data-qa='SignInButton']")).click();
    }, 2000);
    await driver.wait(
      until.elementIsVisible(
        driver.findElement(By.css("div[data-qa='launch-pad']"))
      ),
      4000
    );
    await driver.findElement(By.css("div[data-qa='launch-pad']")).click();
  } catch (e) {
    console.log(e);
  }
})();
