import allure
import pytest


@allure.suite("Calculator Test Suite")
@allure.sub_suite("Basic Arithmetic Sub-Suite")
class TestCalculator:

  @allure.title("Test Case: Add two numbers with text attachment")
  @allure.severity(allure.severity_level.CRITICAL)
  def test_addition(self):
    with allure.step("Step 1: Initialize values 2 and 3"):
      a, b = 2, 3
    with allure.step("Step 2: Perform addition"):
      result = a + b

    # Attach custom text/logs to the Allure report
    allure.attach(
        f"Input values: a={a}, b={b}\nComputed Result: {result}",
        name="Addition Calculation Log",
        attachment_type=allure.attachment_type.TEXT,
    )

    with allure.step("Step 3: Assert result equals 5"):
      assert result == 5

  @allure.title("Test Case: Subtract two numbers")
  @allure.severity(allure.severity_level.NORMAL)
  def test_subtraction(self):
    with allure.step("Step 1: Initialize values 10 and 4"):
      a, b = 10, 4
    with allure.step("Step 2: Perform subtraction"):
      result = a - b
    with allure.step("Step 3: Assert result equals 6"):
      assert result == 6


@allure.suite("String Operations Test Suite")
@allure.sub_suite("Text Formatting Sub-Suite")
class TestStringOperations:

  @allure.title("Test Case: Convert string to uppercase with HTML attachment")
  @allure.severity(allure.severity_level.MINOR)
  def test_string_upper(self):
    with allure.step("Step 1: Define input string"):
      text = "jenkins"
    with allure.step("Step 2: Convert string to upper case"):
      result = text.upper()

    # Attach an HTML snippet artifact to the Allure report
    allure.attach(
        "<h3>Execution Details</h3><p>Original: jenkins</p><p>Converted:"
        f" {result}</p>",
        name="HTML Summary Artifact",
        attachment_type=allure.attachment_type.HTML,
    )

    with allure.step("Step 3: Verify output matches expected uppercase"):
      assert result == "JENKINS"