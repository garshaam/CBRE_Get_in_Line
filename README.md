# CBRE_Get_in_Line
Image to text processor using Tesseract that attempts to preserve the order of messages in a conversation.

## Inspiration
The CBRE challenge seemed like a good way to create a command line project that would be interesting. It was also a good way to learn more about using python to access the file system.

## What it does
Accesses a user-specified directory and converts each image to text using the tesseract library. Separates each “bubble” into a separate message by analyzing line spacing.

## How we built it
We used Visual Studio Code to allow for everyone to work together on the code and created the code using python.

## Challenges we ran into
At the outset, our program printed an unusual string for each comic analyzed. Troubleshooting revealed that tesseract worked properly outside of the main loop. We discovered that our loop was mistakenly printing the last comic by name alphabetically instead of looping through each comic.

## Accomplishments that we're proud of
Fixing the core loop, properly reading images using an unfamiliar library, and working on some side projects related to data.

## What we learned
We learned how to code as a group and use different techniques to make an image appear as text.

## What's next for Queue T(esseract)
We had a very enjoyable time and learned a lot through coding and doing the challenges for image tracking. Now we plan to use this knowledge to work towards new projects revolving around image tracking. We could create a tool using machine learning libraries to classify objects, bodies of text, or solve relevant problems.

