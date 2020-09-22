# clean-code-fundamentals

A short workshop series on coding heuristics, intended to help people of all coding skill levels write cleaner, more maintainable code.  The content is primarily based on the book _Clean Code: A Handbook of Agile Software Craftsmanship_ by Robert C. Martin.  The primary audience for this series is data science and other professionals who might write code in their day-to-day work, but who are interested in making their code easier to maintain, read, and transfer to other people.

## What this isn't...

This is not a computer science course.  This will not teach you the inner workings of a specific programming language, or how to take your code to millisecond response times.  This will not make your code impervious to bugs, server outages, hackers, or PEBCAK errors.  Luckily, if you want to learn those things there are many very smart people on the internet that can help teach you those skills.

## What this is...

This is intended to share a series of coding heuristics, that have been impressed upon me by previous mentors, managers and coworkers, all who make frequent reference to writing software as a craft, as skills to be honed over time, shared with others, and to be deliberately revisited as new tools and techniques are introduced.  I have found the _Clean Code_ book one of many great resources for programmers to build a shared lexicon to identify, discuss and target technical debt and questionable programming decisions.  That being said, I believe these skills are directly transferable to Data Science professionals and can help anyone write better code.

## Sessions

The discussion(s) is structured as four one hour blocks, intended to cover the following topics.

1. **Introduction & Naming Things**
    - <https://bcbeidel.github.io/clean-code-fundamentals/01-introduction-and-naming-things.html>
    - Associated Reading(s): 
        - Clean Code: Introduction (p.7-17) 
        - Clean Code: Meaningful Names (p. 17-30)
2. **Functions**
    - <https://bcbeidel.github.io/clean-code-fundamentals/02-functions-friend-or-foe.html>
    - Associated Reading(s): 
        - Clean Code: Functions (p. 31-52)
3. **Testing**
    - <https://bcbeidel.github.io/clean-code-fundamentals/03-tests-as-insurance.html>
    - Associated Reading(s): 
        - Clean Code: Unit Tests (p. 121-133)
3. **Exceptions, Boundaries, Polymorphism**
    - <https://bcbeidel.github.io/clean-code-fundamentals/04-exceptions-boundaries-dependencies.html>
    - Associated Readings(s):
        - Clean Code: Error Handling (p. 103-112)
        - Clean Code: Boundaries (p. 113-120)

Each discussion is accompanied by an associated reading and a few short coding exercises.  In addition, prior to starting, each participant is encouraged to submit a block of code that they would like to refactor over the course of the discussions (50 - 100 lines).  During the hour, some time will be allocated to review the code in pairs and discuss how it could be improved based on the discussion.  Code examples will be in `R` but many of the principals are the same.

## Preparation

To get the most out of each session, participants are encouraged to:

- Identify and bring a block of code (50 to 100 lines) to refactor during the hour
- Complete the readings associated with each section

## Sources

When preparing for these discussions, these are the resources I leaned on the most.

- Martin, Robert C., and Lei Han. _Clean Code: A Handbook of Agile Software Craftsmanship._
- Mortimer, Adler J., Charles Van Doren. _How to Read a Book: The Classic Guide to Intelligent Reading_

## Other seemingly trivial things that bother programmers...

- [Of Spaces, underscores, and dashes](https://blog.codinghorror.com/of-spaces-underscores-and-dashes/)
- [Which programming case is correct](https://www.reddit.com/r/ProgrammerHumor/comments/5iqykw/vs_help_me_settle_the_age_old_programming_case/)
  - Hint: It depends.
- Single Responsibility Principle --> [Curly's Law: Do One Thing](https://blog.codinghorror.com/curlys-law-do-one-thing/)
- Style Guides: Read one, please.
  - R
    - [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml)
    - [Hadley Wickham: Advanced R](http://adv-r.had.co.nz/Style.html)
    - [Tidyverse Style Guide](https://style.tidyverse.org/)
  - Python
    - [Google's Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
    - [The Hitchhiker Guide to Python](https://docs.python-guide.org/writing/style/)
    - [PEP 8](https://www.python.org/dev/peps/pep-0008/)

## Contributors

Brandon Beidel (bbeidel@redventures.com)
