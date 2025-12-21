# Multi-Agent-Financial-Intelligence-System
**Multi-Agent Financial Intelligence System
Overview**

This project implements a multi-agent AI system that autonomously gathers, analyzes, and summarizes financial analyst recommendations and latest company news for publicly traded stocks (e.g., NVIDIA – NVDA).

Using Phi agents, Groq LLMs, and real-time financial and web data tools, the system collaborates across specialized agents to deliver structured, source-backed financial insights in a single response.

**What This Project Does**

* Retrieves analyst recommendations (buy/hold/sell trends)

* Fetches real-time stock fundamentals and prices

* Aggregates latest company-specific news

* Performs web search with source attribution

* Presents results in clear, tabular, markdown-formatted output

* Demonstrates multi-agent collaboration in an AI system

System Architecture

The project is built using three AI agents, each with a distinct responsibility:

**1. Web Search Agent**

* Searches the web using DuckDuckGo

* Gathers relevant company news

* Always includes sources for traceability

**2. Finance AI Agent**
Uses Yahoo Finance APIs

Retrieves:Stock price data, Analyst recommendations, Company fundamentals, Latest financial news, Displays outputs in structured tables

**3. Multi-Agent Coordinator**

* Orchestrates collaboration between agents

* Merges financial data and web insights

* Ensures consistent formatting and sourcing

**Technologies Used**

* Python

* Phi Framework (Agent orchestration)

* Groq LLM (LLaMA-3 70B)

* Yahoo Finance API

* DuckDuckGo Search Tool

* Markdown-based output rendering

<img width="794" height="406" alt="image" src="https://github.com/user-attachments/assets/1f0c43fe-47b3-4fdd-a355-2d2d05dfe60a" />


<img width="815" height="374" alt="image" src="https://github.com/user-attachments/assets/eb8e9b28-6f00-44a4-b79c-0a1323a41fcd" />


**Example Use Case**

**This system can be used by:**

* Financial analysts for quick stock sentiment checks

* Investors tracking analyst confidence and news momentum

* Data scientists exploring multi-agent AI architectures

* Engineers building AI-powered decision support systems




