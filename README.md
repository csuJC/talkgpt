# TalkGPT: Local Talking LLM with Alibaba Cloud TTS

TalkGPT 是一个结合本地大语言模型和阿里云语音合成 API 的项目，能够实现语音对话功能。此项目基于 [local-talking-llm](https://github.com/vndee/local-talking-llm) 修改，并引入了阿里云 TTS 模块进行语音合成。

---

## 功能特点
- 本地运行大语言模型，通过语音和文本交互。
- 使用阿里云的语音合成（TTS）将助手回答转化为语音。
- 语音输入实时转文字，并生成智能回答。

---

## 环境要求
- **Python 版本**：`3.11`
- **操作系统**：支持 macOS、Linux 和 Windows
- **必要工具**：
  - Poetry (Python 包管理工具)
  - Git
  - pip

---

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/your-username/talkgpt.git
cd talkgpt
conda create -n talkgpt python==3.11
conda activate talkgpt
pip install poetry
poetry install
```


### 2. 配置阿里云服务
	1.	登录 [text](https://nls-portal.console.aliyun.com/applist)。
	2.	创建或选择已有的项目，获取 AppKey。
	3.	参考获取 Token 概述获取 Token。


### 3. 修改appkey和token
    在app.py相应位置修改。

### 4.运行项目！

```bash
    poetry run python app.py
```

### 5.贡献

欢迎提交 Issue 和 Pull Request 改进项目。😊

