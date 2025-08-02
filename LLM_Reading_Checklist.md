# LLM Reading Checklist

Use `+` to mark completed items and add the date when finished.

## Phase 1: Foundational Knowledge

### 1. Introduction to LLMs
- [+] [LLM Concepts](/01.大语言模型基础/1.llm概念/1.llm概念.md) | Date:20250802
- [+] [Language Models](/01.大语言模型基础/1.语言模型/1.语言模型.md) | Date: 20250802
- [+] [Why Decoder-Only Architecture?](/01.大语言模型基础/LLM为什么Decoder-only架构/LLM为什么Decoder-only架构.md) | Date: 20250802

### 2. NLP Basics
- [+] [Tokenization](/01.大语言模型基础/1.分词/1.分词.md) | Date: 20250802
- [+] [Jieba Tokenization](/01.大语言模型基础/2.jieba分词用法及原理/2.jieba分词用法及原理.md) | Date: 20250802
- [+] [Part-of-Speech Tagging](/01.大语言模型基础/3.词性标注/3.词性标注.md) | Date: 20250802
- [+] [Syntax Analysis](/01.大语言模型基础/4.句法分析/4.句法分析.md) | Date: 20250802
- [+] [Word Embeddings](/01.大语言模型基础/5.词向量/5.词向量.md) | Date: 20250802
- [+] [Word2Vec](/01.大语言模型基础/Word2Vec/Word2Vec.md) | Date: 20250802

### 3. Feature Extractors
- [+] [NLP Feature Extractors (CNN, RNN, TF)](/01.大语言模型基础/NLP三大特征抽取器（CNN-RNN-TF）/NLP三大特征抽取器（CNN-RNN-TF）.md) | Date: 20280802

## Phase 2: Core LLM Architecture

### 1. Transformer Basics
- [ ] [Attention Mechanism](/02.大语言模型架构/1.attention/1.attention.md) | Date: _____
- [ ] [Positional Encoding](/02.大语言模型架构/3.位置编码/3.位置编码.md) | Date: _____
- [ ] [Transformer Architecture Details](/02.大语言模型架构/Transformer架构细节/Transformer架构细节.md) | Date: _____

### 2. Advanced Architectures
- [ ] [BERT Details](/02.大语言模型架构/bert细节/bert细节.md) | Date: _____
- [ ] [BERT Variants](/02.大语言模型架构/bert变种/bert变种.md) | Date: _____
- [ ] [LLaMA Series](/02.大语言模型架构/llama系列模型/llama系列模型.md) | Date: _____
- [ ] [LLaMA 2 Code Explanation](</02.大语言模型架构/llama 2代码详解/llama 2代码详解.md>) | Date: _____
- [ ] [LLaMA 3](</02.大语言模型架构/llama 3/llama 3.md>) | Date: _____

### 3. Attention Variants
- [ ] [MHA, MQA, GQA](/02.大语言模型架构/MHA_MQA_GQA/MHA_MQA_GQA.md) | Date: _____

## Phase 3: Training and Optimization

### 1. Distributed Training
- [ ] [Overview](/04.分布式训练/1.概述/1.概述.md) | Date: _____
- [ ] [Data Parallelism](/04.分布式训练/2.数据并行/2.数据并行.md) | Date: _____
- [ ] [Pipeline Parallelism](/04.分布式训练/3.流水线并行/3.流水线并行.md) | Date: _____
- [ ] [Tensor Parallelism](/04.分布式训练/4.张量并行/4.张量并行.md) | Date: _____
- [ ] [Sequence Parallelism](/04.分布式训练/5.序列并行/5.序列并行.md) | Date: _____
- [ ] [Multi-Dimensional Hybrid Parallelism](/04.分布式训练/6.多维度混合并行/6.多维度混合并行.md) | Date: _____
- [ ] [Automatic Parallelism](/04.分布式训练/7.自动并行/7.自动并行.md) | Date: _____
- [ ] [MoE Parallelism](/04.分布式训练/8.moe并行/8.moe并行.md) | Date: _____
- [ ] [Summary](/04.分布式训练/9.总结/9.总结.md) | Date: _____

### 2. Fine-tuning
- [ ] [Basic Concepts](/05.有监督微调/1.基本概念/1.基本概念.md) | Date: _____
- [ ] [Fine-tuning](/05.有监督微调/1.微调/1.微调.md) | Date: _____
- [ ] [LoRA](/05.有监督微调/4.lora/4.lora.md) | Date: _____
- [ ] [ChatGLM3 Fine-tuning](/05.有监督微调/ChatGLM3微调/ChatGLM3微调.md) | Date: _____
- [ ] [LLaMA2 Fine-tuning](/05.有监督微调/llama2微调/llama2微调.md) | Date: _____

## Phase 4: Inference and Applications

### 1. Inference Optimization
- [ ] [Inference Basics](/06.推理/1.推理/1.推理.md) | Date: _____
- [ ] [LLM Inference Optimization](/06.推理/llm推理优化技术/llm推理优化技术.md) | Date: _____
- [ ] [Common Inference Parameters](/06.推理/LLM推理常见参数/LLM推理常见参数.md) | Date: _____

### 2. Reinforcement Learning
- [ ] [RLHF](/07.强化学习/1.rlhf相关/1.rlhf相关.md) | Date: _____
- [ ] [PPO for RLHF](/07.强化学习/大模型RLHF：PPO原理与源码解读/大模型RLHF：PPO原理与源码解读.md) | Date: _____

### 3. Retrieval-Augmented Generation (RAG)
- [ ] [RAG Technology](/08.检索增强rag/rag（检索增强生成）技术/rag（检索增强生成）技术.md) | Date: _____
- [ ] [RAG for LLMs](/08.检索增强rag/检索增强llm/检索增强llm.md) | Date: _____

### 4. Evaluation and Applications
- [ ] [Evaluation](/09.大语言模型评估/1.评测/1.评测.md) | Date: _____
- [ ] [Chain-of-Thought (CoT)](/10.大语言模型应用/1.思维链（cot）/1.思维链（cot）.md) | Date: _____
- [ ] [LangChain](/10.大语言模型应用/1.langchain/1.langchain.md) | Date: _____

## How to Use This Checklist
1. Replace `[ ]` with `[+]` when you complete a topic.
2. Add the date in the `Date: _____` field.
3. Track your progress systematically.