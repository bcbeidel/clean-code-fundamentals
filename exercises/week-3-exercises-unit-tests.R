#' Week 3 | Unit Testing | Exercise
#' ----------------------------------------------------------------------------- 
#' Unit testing is a tool that can help provide additional assurance that code
#' is functioning as expected.  `testthat` is a powerful automated testing tool
#' in R that helps ensure that your small, modular, well-written functions do 
#' the things you say they do.
#' ----------------------------------------------------------------------------- 
#' testthat is required to run this script. Install it. Library it.
#' https://github.com/r-lib/testthat
install.packages("testthat")
library(testthat)

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
add_two_numbers = function(a, b){
  return(a - b)
}

#' This is a passing test.  Run these lines, nothing bad should happen.
testthat::test_that("Ensure one plus zero is one", {
  expected = 1
  actual   = add_two_numbers(1, 0)
  testthat::expect_true(actual == expected)
})

#' This is a failing test.
testthat::test_that("Ensure two plus two is four.", {
  expected = 4
  actual   = add_two_numbers(2, 2)
  testthat::expect_true(actual == expected)
})

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
get_greeting = function(hour_of_day){
  if (hour_of_day < 3) {
    return("Good night.")
  }
  if (hour_of_day < 12) {
    return("Good morning")
  }
  if (hour_of_day < 17) {
    return("Good afternoon")
  }
  return("Good night.")
}

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

