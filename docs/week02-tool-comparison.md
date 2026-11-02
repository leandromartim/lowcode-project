
# Week 2 — AI Tool Comparison

## Tools Used

- Claude (Anthropic)
- Gemini (Google)

Both tools received the same prompt to create a contact form using Flask 3.x and Jinja2.

The original prompts and generated code are saved in the `experiments/week02/` folder.

## Test Results

| Test | Claude | Gemini |
|---|---|---|
| Contact page loads | Pass | Pass |
| Empty fields rejected | Pass | Pass |
| Invalid email rejected | Pass | Pass |
| Valid submission | Pass | Pass |
| JavaScript input test | No execution observed | No execution observed |
| HTTP status for invalid form | 400 | 200 |

## 1. Correctness

Both applications worked during the main tests. They displayed the contact form, validated the required fields and showed a confirmation page after a valid submission.

Claude returned HTTP 400 for invalid data, while Gemini returned HTTP 200. Gemini also provided an incorrect local URL in its instructions.

## 2. Code Quality

Both tools generated readable Python and HTML code.

Claude used a separate validation function, making the code easier to understand and maintain. Gemini placed the validation rules directly inside the contact route.

## 3. Completeness

Both tools included the three required fields: Name, Email and Message.

They also provided server-side validation, error messages and confirmation pages. Neither implementation stores or sends the submitted data.

## 4. Security

Both applications used Jinja2 templates, which escape HTML in normal template expressions.

During our JavaScript input test, neither application displayed a JavaScript alert. However, this test alone does not prove that the applications are fully secure.

Both applications used debug mode. Gemini also included a hard-coded secret key. Neither application included CSRF protection.

## Final Decision

I would choose Claude's implementation for this exercise.

Both applications passed the main functional tests, but Claude provided better HTTP error handling and separated the validation logic into a function.

I also found Claude's implementation easier to understand as a beginner.

## What I Learned

Using the same prompt with different AI tools can produce different code and results.

I learned that AI-generated code should be tested and reviewed instead of being accepted without checking.
