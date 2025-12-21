# Multi-Agent-Financial-Intelligence-System
📊 Multi-Agent Financial Intelligence System
Overview

This project implements a multi-agent AI system that autonomously gathers, analyzes, and summarizes financial analyst recommendations and latest company news for publicly traded stocks (e.g., NVIDIA – NVDA).

Using Phi agents, Groq LLMs, and real-time financial and web data tools, the system collaborates across specialized agents to deliver structured, source-backed financial insights in a single response.

🔍 What This Project Does

Retrieves analyst recommendations (buy/hold/sell trends)

Fetches real-time stock fundamentals and prices

Aggregates latest company-specific news

Performs web search with source attribution

Presents results in clear, tabular, markdown-formatted output

Demonstrates multi-agent collaboration in an AI system

🧠 System Architecture

The project is built using three AI agents, each with a distinct responsibility:

1. Web Search Agent

Searches the web using DuckDuckGo

Gathers relevant company news

Always includes sources for traceability

2. Finance AI Agent

Uses Yahoo Finance APIs

Retrieves:

Stock price data

Analyst recommendations

Company fundamentals

Latest financial news

Displays outputs in structured tables

3. Multi-Agent Coordinator

Orchestrates collaboration between agents

Merges financial data and web insights

Ensures consistent formatting and sourcing

🛠️ Technologies Used

Python

Phi Framework (Agent orchestration)

Groq LLM (LLaMA-3 70B)

Yahoo Finance API

DuckDuckGo Search Tool

Markdown-based output rendering

📁 Project Structure
├── agents.py              # Agent definitions and configurations
├── main.py                # Entry point to run the multi-agent system
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

▶️ How to Run the Project

Install Dependencies

pip install -r requirements.txt


Run the Agent System

multi_ai_agent.print_response(
    "Summarize analyst recommendation and share the latest news for NVDA",
    stream=True
)


View Output

Analyst recommendations in tables

Latest news with sources

Combined insights from multiple agents

📈 Example Use Case

This system can be used by:

Financial analysts for quick stock sentiment checks

Investors tracking analyst confidence and news momentum

Data scientists exploring multi-agent AI architectures

Engineers building AI-powered decision support systems

🚀 Key Learning Outcomes

Designing collaborative multi-agent systems

Integrating LLMs with real-time financial APIs

Structuring AI outputs for business readability

Implementing tool-augmented reasoning with agents

📌 Future Enhancements

Add sentiment analysis for news articles

Support multiple tickers in one query

Export results to PDF or PowerPoint

Add caching to reduce API calls

Deploy as a web app or API service
