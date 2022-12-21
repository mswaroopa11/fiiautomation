from optparse import make_option
import behave
import json
from paver.setuputils import setup
from paver.easy import *
# from paver.easy import task
# from paver.easy import consume_nargs
# from paver.easy import sh
# from paver.easy import cmdopts
import threading, os, platform
from os.path import isfile, join

setup(
    name="uptogether-lambda-test",
    version="1.0.0",
    url="https://www.lambdatest.com/",
    author="Lambdatest",
    description=("Behave Integration with Lambdatest"),
    license="MIT",
    author_email="support@lambdatest.com",
    packages=['features'],
)


def run_behave_test(configFileName, task_id=0, tags="all", device="web", env="develop", suite_name="CONFIG_BUILD",
                    featureName="notset"):
    if tags == "all":
        if platform.system() == 'Windows':
            sh('SET CONFIG_FILE=config/%s.json & SET TASK_ID=%s & SET SUITE_NAME=%s & behave --no-skipped -D device=%s -D env=%s features/%s.feature' % (
                configFileName, task_id, suite_name, device, env, featureName))
        else:
            sh('export CONFIG_FILE=config/%s.json && export TASK_ID=%s && export SUITE_NAME=%s && behave --no-skipped -D device=%s -D env=%s features/%s.feature' % (
                configFileName, task_id, suite_name, device, env, featureName))
    else:
        if platform.system() == 'Windows':
            sh('SET CONFIG_FILE=config/%s.json & SET TASK_ID=%s & SET SUITE_NAME=%s & behave --no-skipped -D device=%s -D env=%s --tags=%s' % (
                configFileName, task_id, suite_name, device, env, tags))
        else:
            sh('export CONFIG_FILE=config/%s.json && export TASK_ID=%s && export SUITE_NAME=%s && behave --no-skipped -D device=%s -D env=%s --tags=%s' % (
                configFileName, task_id, suite_name, device, env, tags))


def lambda_run(configFileName, tags, device, env, suite_name, featureName="notset"):
    filePath = open('config/' + configFileName + '.json')
    fileData = json.load(filePath)
    env_details = fileData['environments']
    parallelLevel = len(env_details)

    if parallelLevel == 1:
        run_behave_test(configFileName, 0, tags, device, env, suite_name, featureName)
    else:
        jobs = []
        for i in range(2):
            p = threading.Thread(target=run_behave_test,
                                 args=(configFileName, i, tags, device, env, suite_name, featureName))
            jobs.append(p)
            p.start()

        for th in jobs:
            th.join()


def local_run(configFileName, device, env, tags="all", featureName="notset"):
    if tags == "all":
        if platform.system() == 'Windows':
            sh('SET CONFIG_FILE=config/%s.json & behave --no-skipped -D device=%s -D env=%s features/%s.feature' % (
                configFileName, device, env, featureName))
        else:
            sh('export CONFIG_FILE=config/%s.json && behave --no-skipped -D device=%s -D env=%s features/%s.feature' % (
                configFileName, device, env, featureName))
    else:
        if platform.system() == 'Windows':
            sh('SET CONFIG_FILE=config/%s.json & behave --no-skipped -D device=%s -D env=%s --tags=%s' % (
                configFileName, device, env, tags))
        else:
            sh('export CONFIG_FILE=config/%s.json && behave --no-skipped -D device=%s -D env=%s --tags=%s' % (
                configFileName, device, env, tags))


@task
def local_web_dev_run_all():
    """Run All develop test cases locally"""
    feature_dir = "features"
    all_dir = os.listdir(feature_dir)
    all_files = [f for f in all_dir if isfile(join(feature_dir, f))]
    feature_files = [f for f in all_files if f.split(".")[1] == "feature"]
    for feature_file in feature_files:
        local_run("local_web", "web", "develop", "all", feature_file.split(".")[0])


@task
def local_web_prod_run_all():
    """Run All prod test cases locally"""
    feature_dir = "features"
    all_dir = os.listdir(feature_dir)
    all_files = [f for f in all_dir if isfile(join(feature_dir, f))]
    feature_files = [f for f in all_files if f.split(".")[1] == "feature"]
    for feature_file in feature_files:
        local_run("local_web", "web", "prod", "all", feature_file.split(".")[0])


@task
@consume_nargs(1)
def local_web_dev_run_tags(args):
    """Run local tag"""
    local_run("local_web", "web", "develop", args[0])


@task
@consume_nargs(1)
def local_web_prod_run_tags(args):
    """Run local tag"""
    local_run("local_web", "web", "prod", args[0])


@task
@consume_nargs(1)
def local_android_dev_run_tags(args):
    """Run local Android dev tag"""
    tags = args[0]
    local_run("local_android", "android", "develop", tags)


@task
@consume_nargs(1)
def local_android_prod_run_tags(args):
    """Run local Android prod tag"""
    tags = args[0]
    local_run("local_android", "android", "prod", tags)


@task
@consume_nargs(1)
def local_ios_dev_run_tags(args):
    """Run local ios dev tag"""
    tags = args[0]
    local_run("local_ios", "ios", "develop", tags)


@task
@consume_nargs(1)
def local_ios_prod_run_tags(args):
    """Run local ios prod tag"""
    tags = args[0]
    local_run("local_ios", "ios", "prod", tags)


@task
def local_dry_run():
    """Dry run of all feature file to check for steps which doesn't have step definations"""
    feature_dir = "features"
    all_dir = os.listdir(feature_dir)
    all_files = [f for f in all_dir if isfile(join(feature_dir, f))]
    feature_files = [f for f in all_files if f.split(".")[1] == "feature"]
    for feature_file in feature_files:
        print(feature_file)
        sh("behave --no-skipped --dry-run features/" + feature_file)


@task
def lambda_web_dev_run_all():
    """Run all dev tests in lambda test"""
    feature_dir = "features"
    all_dir = os.listdir(feature_dir)
    all_files = [f for f in all_dir if isfile(join(feature_dir, f))]
    feature_files = [f for f in all_files if f.split(".")[1] == "feature"]
    for feature_file in feature_files:
        sh("paver lambda_web_dev_run_feature " + feature_file.split(".")[0])


@task
def lambda_web_prod_run_all():
    """Run all prod tests in lambda test"""
    feature_dir = "features"
    all_dir = os.listdir(feature_dir)
    all_files = [f for f in all_dir if isfile(join(feature_dir, f))]
    feature_files = [f for f in all_files if f.split(".")[1] == "feature"]
    for feature_file in feature_files:
        sh("paver lambda_web_prod_run_feature " + feature_file.split(".")[0])


@task
@consume_nargs(1)
def lambda_web_dev_run_tags(args):
    """Run dev tests matching the tag in lambda test."""
    tags = args[0]
    if "@" in tags:
        tags = tags[1:]
    lambda_run("parallel", tags, "web", "develop", "dev_" + tags)


@task
@consume_nargs(1)
def lambda_web_dev_run_tags(args):
    """Run dev tests matching the tag in lambda test."""
    tags = args[0]
    if "@" in tags:
        tags = tags[1:]
    lambda_run("parallel", tags, "web", "develop", "dev_" + tags)

@task
@consume_nargs(1)
def lambda_web_dev_run_feature(args):
    featureName = args[0]
    lambda_run("parallel", "all", "web", "develop", "dev_feature_" + featureName, featureName)


@task
@consume_nargs(1)
def lambda_web_prod_run_feature(args):
    featureName = args[0]
    lambda_run("parallel", "all", "web", "prod", "prod_feature_" + featureName, featureName)


@task
@consume_nargs(1)
def lambda_web_dev_run_feature_single(args):
    """Run all dev tests in lambda test with single test for the specified feature"""
    featureName = args[0]
    lambda_run("single", "all", "web", "develop", "dev_feature_single_" + featureName, featureName)


@task
@consume_nargs(1)
def lambda_web_prod_run_feature_single(args):
    """Run all prod tests in lambda test with single test for the specified feature"""
    featureName = args[0]
    lambda_run("single", "all", "web", "prod", "prod_feature_single_" + featureName, featureName)


@task
@consume_nargs(1)
def lambda_android_dev_run_tags(args):
    """Run dev tests matching the tag in lambda test."""
    tags = args[0]
    if "@" in tags:
        tags = tags[1:]
    lambda_run("android", tags, "android", "develop", "android_develop_" + tags)


@task
@consume_nargs(1)
def lambda_android_prod_run_tags(args):
    """Run prod tests matching the tag in lambda test."""
    tags = args[0]
    if "@" in tags:
        tags = tags[1:]
    lambda_run("android", tags, "android", "prod", "android_prod_" + tags)


@task
@consume_nargs(1)
def lambda_ios_dev_run_tags(args):
    """Run dev tests matching the tag in lambda test."""
    tags = args[0]
    if "@" in tags:
        tags = tags[1:]
    lambda_run("ios", tags, "ios", "develop", "ios_develop_" + tags)


@task
@consume_nargs(1)
def lambda_ios_prod_run_tags(args):
    """Run prod tests matching the tag in lambda test."""
    tags = args[0]
    if "@" in tags:
        tags = tags[1:]
    lambda_run("ios", tags, "ios", "prod", "ios_prod_" + tags)


@task
@consume_nargs(1)
def lambda_andriod_dev_run_feature(args):
    """Run all dev tests in lambda test with single test for the specified feature"""
    featureName = args[0]
    lambda_run("android", "all", "android", "develop", "android_develop_feature_" + featureName, featureName)


@task
@consume_nargs(1)
def lambda_andriod_prod_run_feature(args):
    """Run all prod tests in lambda test with single test for the specified feature"""
    featureName = args[0]
    lambda_run("android", "all", "android", "prod", "android_prod_feature_" + featureName, featureName)


@task
@consume_nargs(1)
def lambda_ios_dev_run_feature(args):
    """Run all dev tests in lambda test with single test for the specified feature"""
    featureName = args[0]
    lambda_run("ios", "all", "ios", "develop", "ios_develop_feature_" + featureName, featureName)


@task
@consume_nargs(1)
def lambda_ios_prod_run_feature(args):
    """Run all prod tests in lambda test with single test for the specified feature"""
    featureName = args[0]
    lambda_run("ios", "all", "ios", "prod", "ios_prod_feature_" + featureName, featureName)


@task
@consume_nargs(1)
def lambda_web_dev_tic_run_tags(args):
    """Run develop tic tests matching the tag in lambda test."""
    tags = args[0]
    if "@" in tags:
        tags = tags[1:]
    lambda_run("single", tags, "web", "develop_tic", "prod_" + tags)


@task
@consume_nargs(1)
def local_web_dev_tic_run_tags(args):
    """Run local web develop tic tag"""
    tags = args[0]
    local_run("local_web", "web", "develop_tic", tags)

