![cover-v5-optimized](https://github.com/chainainexus/can20/assets/13230914/f9e19af5-61ba-4119-b926-d10c4c06ebab)

<p align="center">
  📌 <a href="https://can20.ai/blog/introducing-can20-workflow-file-upload-a-demo-on-ai-podcast">Introducing CAN20 Workflow File Upload: Recreate Google NotebookLM Podcast</a>
</p>

<p align="center">
  <a href="https://cloud.can20.ai">CAN20 Cloud</a> ·
  <a href="https://docs.can20.ai/getting-started/install-self-hosted">Self-hosting</a> ·
  <a href="https://docs.can20.ai">Documentation</a> ·
  <a href="https://ucan20.app/chat/22L1zSxg6yW1cWQg">Enterprise inquiry</a>
</p>

<p align="center">
    <a href="https://can20.ai" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/Product-F04438"></a>
    <a href="https://can20.ai/pricing" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/free-pricing?logo=free&color=%20%23155EEF&label=pricing&labelColor=%20%23528bff"></a>
    <a href="https://discord.gg/FngNHpbcY7" target="_blank">
        <img src="https://img.shields.io/discord/1082486657678311454?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
            alt="chat on Discord"></a>
    <a href="https://reddit.com/r/can20ai" target="_blank">  
        <img src="https://img.shields.io/reddit/subreddit-subscribers/can20ai?style=plastic&logo=reddit&label=r%2Fcan20ai&labelColor=white"
            alt="join Reddit"></a>
    <a href="https://twitter.com/intent/follow?screen_name=can20_ai" target="_blank">
        <img src="https://img.shields.io/twitter/follow/can20_ai?logo=X&color=%20%23f5f5f5"
            alt="follow on X(Twitter)"></a>
    <a href="https://hub.docker.com/u/chainainexus" target="_blank">
        <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/chainainexus/can20-web?labelColor=%20%23FDB062&color=%20%23f79009"></a>
    <a href="https://github.com/chainainexus/can20/graphs/commit-activity" target="_blank">
        <img alt="Commits last month" src="https://img.shields.io/github/commit-activity/m/chainainexus/can20?labelColor=%20%2332b583&color=%20%2312b76a"></a>
    <a href="https://github.com/chainainexus/can20/" target="_blank">
        <img alt="Issues closed" src="https://img.shields.io/github/issues-search?query=repo%3Achainainexus%2Fcan20%20is%3Aclosed&label=issues%20closed&labelColor=%20%237d89b0&color=%20%235d6b98"></a>
    <a href="https://github.com/chainainexus/can20/discussions/" target="_blank">
        <img alt="Discussion posts" src="https://img.shields.io/github/discussions/chainainexus/can20?labelColor=%20%239b8afb&color=%20%237a5af8"></a>
</p>

# ChainAINexus (CAN)

**A Modular AI + Web3 Architecture for the Next Generation Intent-Centric Platform**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
## Overview

ChainAINexus (CAN) is a revolutionary, modular, and extensible Web3-based platform designed to empower users to effortlessly build complex workflows through a plug-in architecture. It acts as an **Intent-Centric** hub, allowing users to express their needs and have the platform intelligently assemble the necessary tools to fulfill them.

Instead of developing monolithic applications, developers can focus on creating single-functionality plugins, significantly lowering the barrier to entry and fostering a vibrant ecosystem. Users, even without coding experience, can then leverage the intuitive **Plugin Canvas** to visually arrange and combine these plugins, creating custom solutions tailored to their specific requirements.

The modularity of CAN not only accelerates development but also unlocks unprecedented flexibility. Plugins can freely interact and be combined in countless ways, allowing the platform to adapt to a vast spectrum of use cases. As the plugin ecosystem grows, so does the potential for innovation, fueled by the exponentially increasing possibilities of plugin combinations. Furthermore, CAN leverages these user-created workflows to train its AI models, progressively enhancing its automation capabilities and eventually enabling the system to intelligently suggest and even automatically generate plugin combinations based on user intent.

## System Architecture

The architecture is divided into three main layers:

**1. User Layer:**

*   **User Interaction:**  Google Chrome Extension, Dapp, Web Interface, Natural Language Interface
*   **Identity Management:** User Identity, Single-Sign Wallet, Multi-Sign Wallet, DID

**2. Application Layer:**

*   **AI Services:** Intention Recognition, Sentiment Analysis, Natural Language Generation
*   **Transaction Tools:** Smart Contract Audit, Content Recommendation, Wallet Tracking, Asset Issuance
*   **Data Processing:** On-Chain Data Analysis, Off-Chain Data Analysis, Prediction Analysis, Multimodal Data Processing

**3. CAN Core:**

*   **Plugin Canvas:** Modular Combination, Logic Control, Data Flow Management, Permission Management, Security Check
*   **Plugin Store:** Upload & Review, Community Ecosystem, Search & Recommendation, Payment Management, Rating System
*   **Plugin Library:** Plugin Management, Storage & Distribution, Developer Support, Plugin Orchestration Library
*   **Contract Library:** Governance Contract, Staking Contract, Revenue Sharing Contract, CAN PROTOCOL, Algorithm Library (NLP, Diffusion Models, TGAN, TTS)

**Visual Representation:**
![CAN Architecture Diagram](https://i.imgur.com/8j7lD9p.png)

## Key Features

*   **Modular Plugin System:**
    *   Developers can focus on building single-function, PMF-driven plugins.
    *   Plugins can interact and be combined freely, enabling complex workflow creation.
    *   Users can visually assemble workflows through a drag-and-drop interface (Plugin Canvas).

*   **Thriving Plugin Ecosystem & AI-Powered Automation:**
    *   A dedicated **Plugin Store** facilitates plugin discovery, distribution, and monetization for developers.
    *   CAN leverages user-created workflows to train AI models, enabling intelligent intent recognition and automated plugin combination recommendations.

*   **Seamless Integration of Web3 and AI:**
    *   Comprehensive support for on-chain and off-chain data analysis, smart contract tools, asset management, and predictive analytics.
    *   The modular architecture bridges the gap between Web3 projects and cutting-edge AI technologies, fostering the development of next-generation decentralized applications.

## Technology Stack

CAN utilizes a robust and versatile technology stack:

*   **Smart Contract Development:** Solidity
*   **Artificial Intelligence:** Python (TensorFlow, PyTorch)
*   **Frontend:** React.js / Next.js
*   **Backend:** Node.js / Express.js
*   **Database:** MongoDB / PostgreSQL
*   **Blockchain Interaction:** Web3.js / ethers.js
*   **Containerization:** Docker

## Getting Started

*   **Developers:**
    *   Refer to the [Developer Documentation](docs/developer_guide.md) (coming soon) to learn how to build and deploy plugins.
    *   Explore the [Plugin API Reference](docs/api_reference.md) (coming soon).
*   **Users:**
    *   Visit the [CAN Website](link-to-website) (coming soon) to access the Plugin Canvas and start building your workflows.
    *   Browse the [Plugin Store](link-to-plugin-store) (coming soon) to discover available plugins.

## Contributing

We welcome contributions from the community! Please refer to our [Contributing Guidelines](CONTRIBUTING.md) (coming soon) for more information on how to get involved.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

*   [Discord](link-to-discord) (coming soon)
*   [Twitter](link-to-twitter) (coming soon)
*   [Telegram](link-to-telegram) (coming soon)

**Join us in building the future of Intent-Centric, AI-powered Web3 applications with ChainAINexus!**