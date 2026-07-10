# 🔍 BrowserAi

An AI-powered security internet search engine that combines intelligent search capabilities with multi-model AI routing for enhanced security analysis and threat detection.

## Features

- 🔒 **Security Focused**: AI-powered threat detection and vulnerability analysis
- 🤖 **Multi-Model AI**: Intelligent routing between specialized AI models
- 🔍 **Advanced Search**: Context-aware search with security filters
- 📊 **Threat Analysis**: Real-time security threat identification
- 🛡️ **Vulnerability Scanning**: Automated vulnerability detection
- ⚡ **Fast Processing**: Optimized for quick threat response
- 🌐 **Web Integration**: Browser-based security monitoring

## Architecture

### Core Components

1. **ROX Assistant**: AI-powered assistant for intelligent task processing
2. **Model Router**: Dynamically routes tasks to optimal AI models
3. **Security Engine**: Analyzes threats and vulnerabilities
4. **Search Module**: Contextual security-focused search

## Technology Stack

- **Language**: Python 3.8+
- **AI Models**: GPT-4, GPT-4-Code, GPT-4-Analysis
- **Architecture**: Modular multi-model system

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- API keys for AI services (optional for development)

### Setup

```bash
# Clone the repository
git clone https://github.com/ramirezrolando222222-eng/BrowserAi.git
cd BrowserAi

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run the application
python main.py
```

## Project Structure

```
BrowserAi/
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
├── .gitignore
└── src/
    ├── __init__.py
    └── ai/
        ├── __init__.py
        ├── rox_assistant.py      # ROX AI Assistant
        ├── model_router.py       # Intelligent task routing
        └── security_engine.py    # Security analysis
```

## Usage

### Basic Usage

```python
from src.ai.rox_assistant import rox_engine
from src.ai.model_router import router

# Route a coding task
result = router.route_task("coding", "Optimize memory allocation")
print(result)

# Get AI status
status = rox_engine.get_status_update()
print(status)
```

### Command Line

```bash
# Run the main application
python main.py

# The application will:
# 1. Initialize ROX AI Assistant
# 2. Route tasks to appropriate models
# 3. Process security analysis
# 4. Return results
```

## API Reference

### ROX Assistant

```python
# Get status update
rox_engine.get_status_update()

# Process a task
rox_engine.process_task("task description")

# Get recommendations
rox_engine.get_recommendations("context")
```

### Model Router

```python
# Route a task
router.route_task("coding", "task description")

# Get optimal model
router.get_optimal_model("coding")

# Add custom model
router.add_model("custom_type", "custom-model-id")

# View routing history
router.get_routing_history(limit=10)
```

## Task Types

The Model Router supports the following task types:

- **coding**: Code analysis and optimization tasks
- **analysis**: Data analysis and report generation
- **creative**: Creative content generation
- **general**: General purpose tasks
- **security**: Security analysis and threat detection

## Configuration

Create a `.env` file for configuration:

```env
AI_MODEL=gpt-4
API_KEY=your_api_key_here
LOG_LEVEL=INFO
DEBUG=false
```

## Examples

### Example 1: Security Analysis

```python
from src.ai.model_router import router

task_description = "Analyze potential SQL injection vulnerabilities"
result = router.route_task("security", task_description)
print(result)
```

### Example 2: Code Optimization

```python
from src.ai.model_router import router

task_description = "Optimize Romux 5 Kernel memory allocation"
result = router.route_task("coding", task_description)
print(result)
```

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

```bash
black src/
flake8 src/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [ ] Real-time threat monitoring
- [ ] Custom security rule engine
- [ ] Integration with external threat databases
- [ ] Web UI dashboard
- [ ] Mobile application
- [ ] Advanced ML models
- [ ] API service

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, and feature requests, please visit the [GitHub Issues](https://github.com/ramirezrolando222222-eng/BrowserAi/issues) page.

## Contact

- Author: ramirezrolando222222-eng
- Email: (add your email)
- GitHub: [@ramirezrolando222222-eng](https://github.com/ramirezrolando222222-eng)

---

**⭐ If you find this project helpful, please consider giving it a star!**
