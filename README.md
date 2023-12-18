# MineDroid
## Problem Statement
 If you're looking to create a chatbot that responds to text queries related to Acts, Rules, and Regulations applicable to the mining industry, you can structure the responses in a clear and user-friendly manner. Here's a simple example of how your chatbot could respond to queries:

User: "What are the key regulations governing mining activities?"

Chatbot: "Hello! In the mining industry, key regulations include the Mines and Minerals (Development and Regulation) Act, which outlines the framework for mining operations. Additionally, environmental aspects are covered by the Environmental Impact Assessment (EIA) notification, ensuring sustainable practices. How can I assist you further?"

User: "Tell me about safety regulations for mining."

Chatbot: "Sure! Safety in mining is a top priority. The Mines Act emphasizes safety standards, covering aspects like ventilation, precautions against fire, and proper lighting. Occupational Safety and Health Administration (OSHA) guidelines are also crucial. If you have specific safety concerns, feel free to ask for more details!"

User: "What environmental rules apply to mining projects?"

Chatbot: "Great question! Mining projects must adhere to environmental regulations like the Forest (Conservation) Act and the Water (Prevention and Control of Pollution) Act. These ensure responsible resource extraction and protection of ecosystems. Anything specific you'd like to know about environmental compliance?"

User: "Can you explain the process of obtaining mining licenses?"

Chatbot: "Absolutely! The Mines and Minerals (Development and Regulation) Act outlines the procedure for obtaining mining licenses. It involves applying to the relevant authorities, submitting environmental impact assessments, and complying with specific criteria. Need more details on the licensing process or any specific stage?"

User: "Tell me about recent changes in mining laws."

Chatbot: "Certainly! As of my last update in January 2022, I recommend checking the latest amendments to the Mines and Minerals (Development and Regulation) Act, as well as any notifications issued by regulatory bodies. Keep in mind that laws may evolve, so staying current is crucial. Is there anything else you'd like to know?"

Remember to update the information regularly to ensure accuracy, and consider incorporating a disclaimer regarding the dynamic nature of legal frameworks. Additionally, tailor the responses based on the specific laws applicable in your jurisdiction.
## Features
1. Answers basic queries pertaining to anything in general like a smart chatbot.
2. Answers queries accurately related to rules, regulations and information about Indian Mining Industries in a detailed manner.

## Local Setup and Installation
 To get the chatbot running locally on your own device, install [Langchain](https://github.com/hwchase17/langchain) and other required dependencies:

```
pip install langchain openai chromadb tiktoken unstructured streamlit googletrans==3.1.0a0
```
Head over to `constants.py` and insert your own [OpenAI API key](https://platform.openai.com/account/api-keys).

To run the pdf_reader:
1. Create a python virtual environment and a .env file
2. Create and insert your own [replicate api key](https://replicate.com/account/api-tokens) as enviornment variable
```
REPLICATE_API_TOKEN = <your replicate api token>
```
3. Finally install all the required dependencies
```
pip install langchain tiktoken replicate streamlit_chat pypdf faiss-cpu sentence_transformers
```
## Running the bot at your terminal:
To run the chatbot load your preferred .txt file.

```
> python chatbotCore.py
Input some text:
```
To run the pdf reader type in the following command at your terminal after following the instructions given in the [Setup section](#local-setup-and-installation)

```
> streamlit run <path of your folder>.venv/pdfbot.py
```
## contribution 
Code Of Conduct-MINEDROID

Our Pledge
In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards
Examples of behavior that contributes to a positive environment for our community include:

Demonstrating empathy and kindness toward other people
Being respectful of differing opinions, viewpoints, and experiences
Giving and gracefully accepting constructive feedback
Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience
Focusing on what is best not just for us as individuals, but for the overall community
Examples of unacceptable behavior include:

The use of sexualized language or imagery, and sexual attention or advances
Trolling, insulting or derogatory comments, and personal or political attacks
Public or private harassment
Publishing others' private information, such as a physical or email address, without their explicit permission
Other conduct which could reasonably be considered inappropriate in a professional setting
Our Responsibilities
Project maintainers are responsible for clarifying and enforcing our standards of acceptable behavior and will take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behavior that they deem inappropriate, threatening, offensive, or harmful.

## Scope
This Code of Conduct applies within all community spaces, and also applies when an individual is officially representing the community in public spaces. Examples of representing our community include using an official e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event.

## Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the community leaders responsible for enforcement . All complaints will be reviewed and investigated promptly and fairly.
### Channels
<a href="https://discord.com/channels/1178241502082768916/1178241502082768920">Discord</a>

## Attribution
This Code of Conduct is adapted from the Contributor Covenant, version 1.4, available at http://contributor-covenant.org/version/1/4

