# README
This is my first attempt at analyzing a data set using NLP (Natural Language Processing) and Python. It uses beatifulsoup and spacy to analyze the top 10 most common social medias' privacy policies. Specifically these privacy policies:
- Snapchat
- Twitter
- Spotify
- Instagram
- Facebook
- Tinder
- Reddit
- Tiktok
- Whatsapp
- Google

# How it works
First I get a .txt representation of every privacy policy.
Then, so that every single sentence isn't being compared to every other sentence, I prune the search space by grabbing every sentence that contains the word "information" (these sentences would probably be the most relevant).
I place these sentences into groups called "blurbs" that are each specific to their respective privacy policy.
Then I compare each blurbs to each other blurb using spacy to find the sentences that are most similiar.
The results are compiled within the "results.txt" document. Sentences with similarities close to 1 are the most similiar.

# Results
See "results.txt"

# Findings
- All services in the data set have the right to hand over your information if law enforcement requests it
- Most services utilize your Advertising ID in targeted ads
  - “It can be sent to advertisers and other third parties which can use this unique ID to track the user's movements, habits, and usages of applications”
- Most of the time if a company is acquired, the acquiring company will be able to obtain your data
- Your information can be processed outside of the US
- Use your information to “improve the safety and reliability of our services”
  - Unclear. Ex:
    - Tinder: The main reason we use your information is to deliver and improve our services. 
    - Twitter: Breaking down how we use the information we collect is not simple because of the way the systems that bring our services to you work.
- If you are banned, services retain information about you.
Device Attributes
  - Type of OS, etc.

# To Run
Clone the repository and run the Tester.py. It takes over 10+ minutes to complete, and the data will be recorded within "results.txt"

