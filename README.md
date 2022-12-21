![Uptogether Lambda Test Automation](https://app.uptogether-feature.org/logo.png)
---

# Uptogether Lambda Test Automation
<br/>


### About Project
- This project is to test Uptogether features via Automated selenium tests using Python and Behave
- This project can be run 
  - Locally 
  - [Lambda Test Website](https://www.lambdatest.com/)

### About Lambda Test
[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can helps to run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. 
#### Features
- It can summaries the test cases based on suite
- It stores the video of the test execution which helps in debugging and locating the defect/bug
- It displayed the timeline and automation logs and reports
- You can login to lambda test using your credentials
  - [Automation](https://automation.lambdatest.com/) tab will display the executions
  - [Dashboard](https://accounts.lambdatest.com/dashboard) tab will display the summary


### Setup
- Install Python 3.9 in your system after downloading from [Website](https://www.python.org/downloads/)
- Install depedencies ```pip install -r requirements.txt```
- It will install all the required dependencies for the project to run

## Run Tests<br/>

## Locally<br/>

### Local Web <br/>
<img src="./images/local.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/dev.png" width="40">
#### To Run all web dev testcases locally  
- It will run all the tests in all feature files in dev environment
- It doesn't take any parameter
```bash
paver local_web_dev_run_all
```
<img src="./images/local.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/prod.png" width="40">
#### To Run all web prod testcases locally
- It will run all the tests in all feature files in prod environment
- It doesn't take any parameter
```bash
paver local_web_prod_run_all
```
<img src="./images/local.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/dev.png" width="40">
#### To Run web dev test cases associated with a tag locally
- It will run all the tests associated with a tag in dev environment
- It take only one parameter, tag_name
```bash
paver local_web_dev_run_tags <tag_name>
```
Ex:
```bash
paver local_web_dev_run_tags @social.group
```
<img src="./images/local.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/prod.png" width="40">
#### To Run web prod test cases associated with a tag locally
- It will run all the tests associated with a tag in prod environment
- It take only one parameter, tag_name
```bash
paver local_web_prod_run_tags <tag_name>
```
Ex:
```bash
paver local_web_prod_run_tags @social.group
```

### Local Mobile Execution
> In order to perform mobile execution you need to install appium and start appium server in 0.0.0.0:4723

> Update the device details in either local_android.json or local_ios.json based on the device in which execution need to be done

<img src="./images/local.jpeg" width="48"><img src="./images/android.png" width="48"><img src="./images/dev.png" width="40">
#### To Run android dev test cases associated with a tag locally
- It will run all the tests associated with a tag in dev environment
- It take only one parameter, tag_name
```bash
paver local_android_dev_run_tags <tag_name>
```
Ex:
```bash
paver local_android_dev_run_tags @social.group
```
<img src="./images/local.jpeg" width="48"><img src="./images/android.png" width="48"><img src="./images/prod.png" width="40">
#### To Run android prod test cases associated with a tag locally
- It will run all the tests associated with a tag in prod environment
- It take only one parameter, tag_name
```bash
paver local_android_prod_run_tags <tag_name>
```
Ex:
```bash
paver local_android_prod_run_tags @social.group
```
<img src="./images/local.jpeg" width="48"><img src="./images/ios.jpeg" width="48"><img src="./images/dev.png" width="40">
#### To Run ios dev test cases associated with a tag locally
- It will run all the tests associated with a tag in dev environment
- It take only one parameter, tag_name
```bash
paver local_ios_dev_run_tags <tag_name>
```
Ex:
```bash
paver local_ios_dev_run_tags @social.group
```
<img src="./images/local.jpeg" width="48"><img src="./images/ios.jpeg" width="48"><img src="./images/prod.png" width="40">
#### To Run ios prod test cases associated with a tag locally
- It will run all the tests associated with a tag in prod environment
- It take only one parameter, tag_name
```bash
paver local_ios_prod_run_tags <tag_name>
```
Ex:
```bash
paver local_ios_prod_run_tags @social.group
```
<img src="./images/local.jpeg" width="60">

#### For dry run locally 
- It will check the entire feature file and report if any of the step is not associalted with step definition
- It doesn't take any parameter
```bash
paver local_dry_run
```
### Executions on Lambda Test<br/>
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/dev.png" width="40">
#### To Run all web dev testcase in lambda test
- It will run all the tests in all feature files in dev environment of lambda test
- It doesn't take any parameter
```bash
paver lambda_web_dev_run_all
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/prod.png" width="40">
#### To Run all web prod testcase in lambda test
- It will run all the tests in all feature files in prod environment of lambda test
- It doesn't take any parameter
```bash
paver lambda_web_prod_run_all
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/dev.png" width="40">
#### To Run dev web test cases associated with a tag in lambda test
- It will run all the prod tests associated with a tag in dev environment of lambda test
- It take only one parameter, tag_name
```bash
paver lambda_web_dev_run_tags <tag_name>
```
Ex:
```bash
paver lambda_web_dev_run_tags @social.group
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/prod.png" width="40">
#### To Run prod test cases associated with a tag in lambda test
- It will run all the dev tests associated with a tag in prod environment of lambda test
- It take only one parameter, tag_name
```bash
paver lambda_web_prod_run_tags <tag_name>
```
Ex:
```bash
paver lambda_web_prod_run_tags @social.group
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/dev.png" width="40">
#### To Run dev web all test cases of a feature in lambda test in parallel
- It will run all the dev tests associated with a feature in parallel
- It take only one parameter, feature_name
```bash
paver lambda_web_dev_run_feature <feature_name>
```
Ex:
```bash
paver lambda_web_dev_run_feature social
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/prod.png" width="40">
#### To Run prod web all test cases of a feature in lambda test in parallel
- It will run all the prod tests associated with a feature in parallel
- It take only one parameter, feature_name
```bash
paver lambda_web_prod_run_feature <feature_name>
```
Ex:
```bash
paver lambda_web_prod_run_feature social
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/dev.png" width="40">
#### To Run dev web all test cases of a feature in lambda test in without parallel
- It will run all the prod tests associated with a feature in chrome
- It take only one parameter, feature_name
```bash
paver lambda_web_dev_run_feature_single <feature_name>
```
Ex:
```bash
paver lambda_web_dev_run_feature_single social
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/web.jpeg" width="48"><img src="./images/prod.png" width="40">
#### To Run prod web all test cases of a feature in lambda test in without parallel
- It will run all the dev tests associated with a feature in chrome
- It take only one parameter, feature_name
```bash
paver lambda_web_prod_run_feature_single <feature_name>
```
Ex:
```bash
paver lambda_web_prod_run_feature_single social
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/android.png" width="48"><img src="./images/dev.png" width="40">
#### To Run android dev test cases associated with a tag in lambda test
- It will run all the tests associated with a tag in dev environment
- It take only one parameter, tag_name
```bash
paver lambda_android_dev_run_tags <tag_name>
```
Ex:
```bash
paver lambda_android_dev_run_tags @social.group
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/android.png" width="48"><img src="./images/prod.png" width="40">
#### To Run android prod test cases associated with a tag lambda test
- It will run all the tests associated with a tag in prod environment
- It take only one parameter, tag_name
```bash
paver lambda_android_prod_run_tags <tag_name>
```
Ex:
```bash
paver lambda_android_prod_run_tags @social.group
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/ios.jpeg" width="48"><img src="./images/dev.png" width="40">
#### To Run ios dev test cases associated with a tag lambda test
- It will run all the tests associated with a tag in dev environment
- It take only one parameter, tag_name
```bash
paver lambda_ios_dev_run_tags <tag_name>
```
Ex:
```bash
paver lambda_ios_dev_run_tags @social.group
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/ios.jpeg" width="48"><img src="./images/prod.png" width="40">
#### To Run ios prod test cases associated with a tag lambda test
- It will run all the tests associated with a tag in prod environment
- It take only one parameter, tag_name
```bash
paver lambda_ios_prod_run_tags <tag_name>
```
Ex:
```bash
paver lambda_ios_prod_run_tags @social.group
```


<img src="./images/lambdatest.jpeg" width="48"><img src="./images/android.png" width="48"><img src="./images/dev.png" width="40">
#### To Run android dev test cases associated with a tag in lambda test
- It will run all the tests associated with a feature in dev environment
- It take only one parameter, feature_name
```bash
paver lambda_andriod_dev_run_feature <feature_name>
```
Ex:
```bash
paver lambda_andriod_dev_run_feature social
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/android.png" width="48"><img src="./images/prod.png" width="40">
#### To Run android prod test cases associated with a tag lambda test
- It will run all the tests associated with a feature in prod environment
- It take only one parameter, feature_name
```bash
paver lambda_andriod_prod_run_feature <feature_name>
```
Ex:
```bash
paver lambda_andriod_prod_run_feature social
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/ios.jpeg" width="48"><img src="./images/dev.png" width="40">
#### To Run ios dev test cases associated with a tag lambda test
- It will run all the tests associated with a feature in dev environment
- It take only one parameter, feature_name
```bash
paver lambda_ios_dev_run_feature <feature_name>
```
Ex:
```bash
paver lambda_ios_dev_run_feature social
```
<img src="./images/lambdatest.jpeg" width="48"><img src="./images/ios.jpeg" width="48"><img src="./images/prod.png" width="40">
#### To Run ios prod test cases associated with a tag lambda test
- It will run all the tests associated with a feature in prod environment
- It take only one parameter, feature_name
```bash
paver lambda_ios_prod_run_feature <feature_name>
```
Ex:
```bash
paver lambda_ios_prod_run_feature social
```

### Configuration steps</br>
#### Setting locally --

- Set LambdaTest username and access key in environment variables. It can be obtained from [LambdaTest dashboard](https://automation.lambdatest.com/)
example:
- For linux/mac
```
   export LT_USERNAME="YOUR_USERNAME"
   export LT_ACCESS_KEY="YOUR_ACCESS_KEY"
  
```
- For Windows
```
   set LT_USERNAME="YOUR_USERNAME"
   set LT_ACCESS_KEY="YOUR_ACCESS_KEY"
  
```
#### Setting for automation --

The configurations are present in `config` folder.
 For setting capaibilies,Update `<file name>.json`  (List of supported OS platfrom, Browser, resolutions can be found at [LambdaTest capability generator](https://www.lambdatest.com/capabilities-generator/))

For Example:

 Setting capabilties for parallel execution in config/parallel.json
```
  {
  "user": "YOUR_USERNAME",
  "key": "YOUR_ACCESS_KEY",
  "capabilities": {
    "build": "behave-test-lambdatest",
    "name": "parallel-test"
  },

  "environments": [{
    "browser": "chrome",
    "tunnel":false,
    "network":false,
    "visual":false
  },{
    "browser": "firefox",
    "tunnel":false,
    "network":false,
    "visual":false

  }
]
```
 Setting capabilties for ios execution in config/ios.json
```
{
  "user": "YOUR_USERNAME",
  "key": "YOUR_ACCESS_KEY",
  "capabilities": {
    "build": "mobile_ios_test",
    "name": "mobile_ios_test",
    "console": true,
    "network": true,
    "platformName": "iOS",
    "deviceName": "iPhone 12",
    "platformVersion": "15.0",
    "appiumVersion": "1.22.1",
    "autoGrantPermissions": true
  },
  "environments": [
    {
      "browser": "Safari",
      "tunnel": false,
      "network": false,
      "visual": false
    }
  ]
}
```
## To create new test
- Add a scenario and add a tag to it in a .feature file in `features` folder
- Add the implementation method in .py file inside `features/steps` folder
- Add the page method in <page_file_name>.py file inside `pages` folder
- Run the test using the tag name of the testcase