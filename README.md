# 🎮 AI Trivia Host

An interactive, conversational trivia game powered by LangGraph and open-source LLMs. The AI hosts a 5-question trivia session, tracks your score in real-time, and delivers a final verdict—all without cloud API costs.

## ✨ Features

- **Conversational Trivia Host** – Engages in natural dialogue while hosting trivia questions
- **Real-time Score Tracking** – Automatically records and displays your score after each question
- **Multi-choice Questions** – AI generates 5 trivia questions with multiple-choice options
- **State Management** – Custom state design for score and question tracking
- **Local LLM** – Powered by Ollama (Qwen 3.5:4B) for privacy and cost-efficiency
- **Session Persistence** – Memory checkpointing for multi-turn conversations

## 🏗️ Architecture

This project demonstrates core LangGraph concepts:

- **StateGraph** – Custom `TriviaState` class extending `MessagesState` for score and question tracking
- **Nodes** – Assistant node handles AI interactions and tool invocation
- **Edges** – Conditional routing between assistant and tool execution
- **Tools** – Function calling for score recording and game state management
- **Checkpointing** – Memory-based session persistence for consistent gameplay

```
START → Assistant → Tools (conditional) → Assistant → END
```

### Key Components

| Component | Purpose |
|-----------|---------|
| `TriviaState` | Extends MessagesState with `score` and `questions_asked` fields |
| `record_score()` | Tool to update user score after each question |
| `isGameOver()` | Tool to signal game completion after 5 questions |
| `assistant()` | LLM-powered node that hosts the trivia game |

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai/) installed and running
- Qwen 3.5:4B model downloaded (`ollama pull qwen3.5:4b`)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jsn-afons/ai_trivia_host.git
cd ai_trivia_host
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start Ollama server:
```bash
ollama serve
```

### Usage

Run the trivia game:
```bash
python main.py
```

Follow the prompts to answer 5 trivia questions. The AI will track your score and announce the final verdict!

## 📚 Tech Stack

- **LangGraph** – Agentic AI framework for building graph-based workflows
- **LangChain** – LLM orchestration and tool management
- **Ollama + Qwen 3.5:4B** – Local, open-source language model
- **Python 3.10+** – Core language

## 🎓 Learning Outcomes

This project demonstrates:
- Building stateful AI agents with LangGraph
- Function calling and tool use for agent capabilities
- Conditional routing in agentic workflows
- Session management and conversation history tracking
- Working with local LLMs for cost-effective AI development

## 🔄 Game Flow

1. User starts the game
2. AI generates and asks Question 1 with multiple-choice options
3. User responds with their answer
4. AI validates the answer and updates score using `record_score()` tool
5. Steps 2-4 repeat until 5 questions are answered
6. AI calls `isGameOver()` tool and announces final score

## 💡 Future Enhancements

- [ ] Add difficulty levels (easy, medium, hard)
- [ ] Persist high scores to a database
- [ ] Add category selection for trivia topics
- [ ] Implement hint system
- [ ] Support for multiple players
- [ ] Web UI with Flask/Streamlit

## 📝 License

MIT

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📧 Questions?

Have questions about LangGraph, AI agents, or this project? Feel free to reach out or open an issue!

---

**Made with ❤️ using LangGraph and open-source AI**
