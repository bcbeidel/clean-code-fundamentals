import unittest


#' Week 3 | Unit Testing | Exercise
#' ----------------------------------------------------------------------------- 
#' Unit testing is a tool that can help provide additional assurance that code
#' is functioning as expected.  `testthat` is a powerful automated testing tool
#' in R that helps ensure that your small, modular, well-written functions do 
#' the things you say they do.
#' ----------------------------------------------------------------------------- 
#' unittest is a built in framework.  Check the docs for more information
#'  and examples https://docs.python.org/2/library/unittest.html
#' ----------------------------------------------------------------------------- 
#' ---------------------------- 1 - Fixing Unit Tests --------------------------
#' ----------------------------------------------------------------------------- 
#' 
#' Directions:
#' 
#' 1. Run the code in the next few lines. Answer the following questions:
#'  - What comes out of the console when you run the first test?
#'  - What information does the console provide when you run the second test?
#' 
#' 2. Refactor `add_two_numbers` so that both tests cases pass
#'  - Rerun the tests, how does the output change in the console?
#' 
def add_two_numbers(a, b):
  return (a - b)

class TestAddTwoNumbers(unittest.TestCase):
    
    #' This is a passing test.  Run this, nothing bad should happen.
    def test_add_two_numbers(self):
        result = add_two_numbers(1, 0)
        self.assertEqual(result, 1)

    #' This is a failing test.
    def test_add_two_numbers_postive_inputs(self):
        result = add_two_numbers(2, 2)
        self.assertEqual(result, 0)

#' -----------------------------------------------------------------------------
#' ---------------------- 2 - Writing Unit Tests -------------------------------
#' -----------------------------------------------------------------------------
#' Based on the trivial example above, we now have an example of the testthat 
#' syntax. Now we write our own.
#' 
#' Exercise:
#' - Based on that syntax write unit tests that help ensure that `get_greeting` 
#'   returns the appropriate greeting at the following times: 5 am, 10 am, 11 pm

#' Takes a numeric hour_of_day, returns the appropriate greeting.
#' 
#'  @param hour_of_day numeric. hour component current time, on 24h clock.
#'                     valid range 0-24
#'  
#'  @return string. Greeting to humans. 
def get_greeting(hour_of_day):
  """ Gets the `time-appropriate` greeting based on the `hour_of_day` """
  
  if hour_of_day < 3:
    return "Good night."
  if hour_of_day < 12:
    return "Good morning."
  if hour_of_day < 17:
    return "Good afternoon."
  return "Good night."

#' -----------------------------------------------------------------------------
#' ---------------------- 3 - Testing the edges --------------------------------
#' -----------------------------------------------------------------------------
#' So our tests above are at seemingly arbitrary times, and might not be the 
#' most effective way to test that times where the behavior of our function is 
#' expected to change.  These points of behavior change are often referred to as 
#' `edge cases`. The following questions are intended to help identify and test 
#' edge cases. Doing so, can help ensure your unit tests catch the full extremes 
#' of functionality
#' 
#' Questions:
#' - Based on the way `get_greeting` is written, what hours of the day do we 
#'   expect the behavior to change?
#' - How does the behavior change if you chose an input just above or below your 
#'   identified `edge cases`?
#' 
#' Exercise:
#' - Write the tests required to validate your edge cases.

class TestGreeting(unittest.TestCase):
    
    #' This is a passing test.  Run this, nothing bad should happen.
    def test_greeting_early(self):
        result = get_greeting(1)
        self.assertEqual(result, "Good night.")

    # add more tests here.

#' -----------------------------------------------------------------------------
#' ---------------------- 4. Bonus Round ---------------------------------------
#' -----------------------------------------------------------------------------
#' Failure is always an option.  Errors can be considered expected behavior.  
#' Our `get_greeting` function hasn't been written in such a way to protect 
#' ourselves from bad inputs. Think values out of range, wrong data types, NA, and NULL. 
#' 
#' Exercise:
#'  - Refactor `get_greeting` to validate the inputs
#'    into the function meet expectations, and if they don't fail appropriately.
#'  - Write unit tests to ensure that your refactored function acts as expected 
#'    with bad inputs. `testthat::expect_error` is your friend here.


if __name__ == '__main__':
    unittest.main()
