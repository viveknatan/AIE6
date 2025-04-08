<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE6/tree/main/00_AIM_Quicklinks)

| 🤓 Pre-work | 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Session 1: Pre-Work](https://www.notion.so/Session-1-Introduction-and-Vibe-Check-1c8cd547af3d81b596bbdfb64cf4fd2f?pvs=4#1c8cd547af3d81fb96b4f625f3f8e3d6)| [Session 1: Introduction and Vibe Check](https://www.notion.so/Session-1-Introduction-and-Vibe-Check-1c8cd547af3d81b596bbdfb64cf4fd2f) | Coming Soon! | Coming Soon! | You Are Here! | [Homework](https://forms.gle/W59zjs5MQc7kbLUh9) | [AIE6 Feedback 4/1](https://forms.gle/EdzBz82yGqVYKfUw9)


### Assignment

In the following assignment, you are required to take the app that you created for the AIE6 challenge (from [this repository](https://github.com/AI-Maker-Space/Beyond-ChatGPT)) and conduct what is known, colloquially, as a "vibe check" on the application. 

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE6/tree/main/00_Setting%20Up%20Git)!

#### How AIM Does Assignments
Throughout our time together - we'll be providing a number of assignments. Each assignment can be split into two broad categories:

- Base Assignment - a more conceptual and theory based assignment focused on locking in specific key concepts and learnings.
- Hardmode Assignment - a more programming focused assignment focused on core code-concepts.

Each assignment will have a few of the following categories of exercises:

- ❓Questions - these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!
- 🏗️ Activities - these will be work or coding activities meant to reinforce specific concepts or theory components.
- 🚧 Advanced Builds - these will only appear in Hardmode assignments, and will require you to build something with little to no help outside of documentation!

##### 🏗️ Activity #1:

Please evaluate your system on the following questions:
Vibe check performed using llm-app :: https://huggingface.co/spaces/vivnatan/llm-app

1. Explain the concept of object-oriented programming in simple terms to a complete beginner. 
    - Aspect Tested: Clarity and Simplicity :: Vibes - Good but could be better. Very clear and linear explanation. But the metaphors used to explain these concepts to a beginner could be more straightforward.
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: Length & Level of Detail :: The original passage has ~580 words and the summary generated has ~270 words which is much longer than ideal. The summary is very detailed and could help a student recap the incident while preparing for a test. It depends on the context and the vibes here is still good but not great. 
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: Creativity and imagination :: Vibes of the story were Mid; very straightforward and expected story. Could be more creative and surprise us.
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: Accuracy & Strucutre :: The problem was correctly solved. However the steps were not very clear and could have been better explained. Vibes are good but could be better.
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: Tone :: The tone of the rewrite is professional, warm and to the point. It could be a touch more detailed and polished and so I feel that there is still room for improvement.

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

##### 🚧 Advanced Build:

Please make adjustments to your application that you believe will improve the vibe check done above, push the changes to your HF Space and redo the above vibe check.

Vibe check performed using llm-app-revised :: https://huggingface.co/spaces/vivnatan/llm-app-revised <br>
Features added: <br>
The llm-app-revised uses LLM to identify the task input by the user <br>
Based on the identified task type, the system settings are varied. <br>
Settings including, temperature, model and max tokens are varied by the task type <br>

1. Explain the concept of object-oriented programming in simple terms to a complete beginner. 
    - Aspect Tested: Clarity and Simplicity :: The explanation is more relatable and engaging to a beginner. The output is clearer and better suited for the target audience.
2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: Length & Level of Detail :: The summary generated has ~130 words which is very compact and efficient. The summary includes the essential details and serves it's purpose.
3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: Creativity and imagination :: Unexpected setting and characters in the short story. Very ceative and imaginative in the way it establishes the setting and surroundings in such a short story.
4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: Accuracy & Strucutre :: The problem was solved correctly and explained clearly. It was segmented into steps which makes it ideal for a student to follow along.
5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: Tone :: Slightly more polished in language and structured in tone.
> NOTE: You may reach for improving the model, changing the prompt, or any other method.

### A Note on Vibe Checking

"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.

In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

##### 🧑‍🤝‍🧑❓ Discussion Question #1:

What are some limitations of vibe checking as an evaluation tool?
