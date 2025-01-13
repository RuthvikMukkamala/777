# The 777 Investment Fund

**Welcome to The 777 Investment Fund** — a purely agentic-driven, multi-strategy, open-source investment firm. This repository is built to operate much like a "pod-shop" trading firm. Here, you can openly contribute new "agent pods" and collaborate in making data-driven investment decisions that aim to generate superior returns.

---

## Table of Contents

1. [Project Vision](#project-vision)  
2. [Architecture Overview](#architecture-overview)  
3. [Teams](#teams)  
   - [Data Team](#data-team)  
   - [Investing Team](#investing-team)  
   - [Execution Team](#execution-team)  
4. [Agentic Design and Pub/Sub Model](#agentic-design-and-pubsub-model)  
5. [How to Contribute](#how-to-contribute)  
6. [Project Roadmap](#project-roadmap)  
7. [License](#license)  

---

## Project Vision

The 777 Investment Fund is **multi-strategy** and **purely agentic**:
- **Multi-strategy**: We incorporate a range of approaches — fundamental analysis, macro strategies, quantitative strategies, and risk management — to make investment decisions.
- **Purely agentic**: The fund is driven by autonomous "agents." These agents (small modular pods) collectively handle everything from data ingestion and analytics to investment decisions and trade execution.

This open-source project invites quants, analysts, developers, and trading enthusiasts to collaborate on building a next-generation platform that leverages autonomous agents for investment decisions. Our aim is to foster an open, innovative environment where **everyone** contributes to a unified investment strategy.

---

## Architecture Overview

We divide the architecture across three main teams (or phases) to structure our workflow:

1. **Data Team**  
2. **Investing Team**  
3. **Execution Team**

Agents (individual code modules) are split by their role in the fund:
- **Technical agents**: Data ingestion, cleaning, feature engineering, etc.  
- **Investing agents**: Fundamental/macro analysis, portfolio optimization, quantitative strategy signals, risk management.  
- **Execution agents**: Order routing, execution optimization, trade surveillance, post-trade analysis.

### High Level Pipeline

1. **Data Collection & Processing**: Data Team  
2. **Investment Decision**: Investing Team  
3. **Trade Execution**: Execution Team  

Each step depends on a robust Pub/Sub mechanism for agent communication (see [Agentic Design and Pub/Sub Model](#agentic-design-and-pubsub-model)).

---

## Teams

### Data Team

- **Objective**: Acquire, clean, and deliver high-quality data in real-time or near real-time.  
- **Data Sources**: We use a variety of data providers such as [OpenBB](https://openbb.co/) and other public or proprietary APIs.  
- **Responsibilities**:  
  - Ingest new data feeds (market data, alternative data, etc.).  
  - Perform data cleaning and normalization.  
  - Publish standardized datasets to the Pub/Sub channels (for the Investing Team and other subscribed agents).

### Investing Team

- **Objective**: Evaluate data-driven insights and decide on potential trades and strategies.  
- **Roles**:  
  - **Fundamental Analysts**: Investigate company/industry fundamentals.  
  - **Macro Strategists**: Assess global economic and market conditions.  
  - **Quantitative Risk Managers**: Ensure that trade exposures and overall portfolio risk align with the fund’s risk profile.  
  - **Portfolio Managers**: Ultimately approve or reject trades proposed by the agents.  
- **Responsibilities**:  
  - Subscribing to data topics published by the Data Team.  
  - Combining fundamental insights, macro analysis, and quantitative signals to form actionable strategies.  
  - Broadcasting investment decisions or trade signals to the Execution Team.

### Execution Team

- **Objective**: Execute trades efficiently and manage post-trade operations.  
- **Roles**:  
  - **Trade Execution Agents**: Route orders to appropriate brokers or exchanges, optimizing for speed, cost, or other metrics.  
  - **Surveillance & Compliance Agents**: Monitor trades for compliance, detect anomalies, etc.  
  - **Post-Trade Analysis**: Provide feedback loop to the Investing Team, including fill prices, slippage, and performance metrics.  
- **Responsibilities**:  
  - Subscribe to the signals and instructions from the Investing Team.  
  - Manage real-time order routing, execution tracking, and trade settlement.  
  - Publish execution data back to the Pub/Sub channels for future analysis and optimization.

---

## Agentic Design and Pub/Sub Model

At the heart of The 777 Investment Fund is a **Pub/Sub architecture**, where agents publish data or signals, and other agents subscribe to those topics.

1. **Publisher**: An agent (e.g., a data ingestion agent) that makes certain data or signals available to the rest of the system.  
2. **Subscriber**: Agents (e.g., the investing team’s fundamental analysis agent) that listen to these data feeds and integrate the information into their own processes.  
3. **Event-driven Workflow**: As soon as new data is published, all subscribed agents can immediately process it, generating near real-time decision-making.

**Example**:  
- **Data Ingestion Agent** fetches the latest market data from OpenBB, publishes it to the `MarketData` topic.  
- **Quant Strategy Agent** subscribes to `MarketData`, runs calculations, publishes new signals to the `SignalQuant` topic.  
- **Portfolio Manager Agent** subscribes to `SignalQuant` and uses those insights to decide on potential trades, which it publishes to the `TradeOrders` topic.  
- **Execution Agent** listens to `TradeOrders` and places the trades, later publishing execution reports on `TradeFills`.

---

