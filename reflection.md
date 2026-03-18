# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  # 1. Fixed - went down to 1 as a guess but still lower, guess number under 1 but instructs to guess between 1 and 100
  # 2. there was 1 attempt left but said it was out of attempts and gave answer
  # 3. the new game button doesnt reset the game after you have won, if you click reset before you win it does reset the game. 
  - Also, new game always generated a secret number in the range 1–100 regardless of difficulty, because it used `random.randint(1, 100)` instead of `random.randint(low, high)`. Fixed by replacing the hardcoded values with the `low` and `high` variables already computed from the selected difficulty.
  # 4. also when you first attempt a guess it does not decrease the number of attempts left until you click the guess button again
  # 5. is the average adding up correctly? the number becomes negative if you fail to guess in time.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

1. I used claude
2. I asked claude to help me understand the functions that are related to the function and walk through the logic. It correctly explained how the secret number was generated and why it was changing. I verified this by looking at the code and seeing that the secret number was being generated inside a function that was called on every rerun, which is why it kept changing.
3. I asked claude to help me fix the issue with the secret number changing and it suggested adding an extra variable to the function definition and I realized that this was not necessary because the `low` and `high` variables were already being computed from the selected difficulty and could be used to generate the secret number. I verified this by looking at the code and seeing that the `low` and `high` variables were already being computed and could be used to generate the secret number without needing an extra variable.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed by running the app and testing the specific functionality as well as using ai to generate pytest cases to test the functionality. 
- Describe at least one test you ran (manual or using pytest)  
I ran a manual test where I selected the easy difficulty and made a guess of 1. The app correctly told me that my guess was too low and that I had 9 attempts left. I then made a guess of 100 and the app correctly told me that my guess was too high and that I had 8 attempts left. This showed me that the secret number was being generated correctly and that the hints were working as expected.
- Did AI help you design or understand any tests? How?
Yes - it helped me understand how to write pytest cases and what to test for.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
