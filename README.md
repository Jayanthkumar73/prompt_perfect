# ✨ Prompt Perfecter

AI-powered prompt engineer that transforms simple prompts into detailed, effective instructions for generative AI models using Google's Gemini 2.5 Pro.

## 🚀 Features

- **Smart Prompt Enhancement**: Automatically adds context, structure, and constraints to your prompts
- **Multiple Gemini Models**: Support for Gemini 2.5 Pro, Flash, and experimental models
- **Secure API Key Management**: Uses environment variables via `.env` file
- **Error Handling**: Robust error handling for API quotas and network issues
- **Easy to Use**: Simple command-line interface

## 📋 Prerequisites

- Python 3.7 or higher
- Google AI API key ([Get one here](https://makersuite.google.com/app/apikey))
- Internet connection

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Prompt-perfect
   ```

2. **Install required packages**
   ```bash
   pip install google-generativeai python-dotenv
   ```

3. **Set up your API key**
   
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```

## 💻 Usage

Run the script:
```bash
python perfecter.py
```

Enter your simple prompt when asked, and the AI will transform it into a detailed, optimized prompt.

### Example

**Input:**
```
write a story about a cat
```

**Output:**
```
Write a heartwarming short story (800-1000 words) about a curious tabby cat 
named Whiskers who discovers a hidden magical garden in their backyard. 
Include:
- A clear beginning, middle, and end structure
- Vivid sensory descriptions of the garden
- Character development showing Whiskers' personality
- A gentle tone suitable for all ages
- Dialogue or internal thoughts from the cat's perspective
Avoid: violence, dark themes, or overly complex vocabulary
```

## 🎯 Available Models

The script currently uses `gemini-2.5-flash`. You can change the model in `perfecter.py`:

- **`gemini-2.5-pro`** - Highest quality, best for complex prompts
- **`gemini-2.5-flash`** - Fast and balanced (default)
- **`gemini-pro-latest`** - Always uses the latest Pro version
- **`gemini-flash-latest`** - Always uses the latest Flash version

To change the model, edit line 37 in `perfecter.py`:
```python
model=genai.GenerativeModel('gemini-2.5-pro')  # Change model name here
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file:
```env
GOOGLE_API_KEY=your_actual_api_key
```

### Security Notes

- ⚠️ Never commit your `.env` file to Git
- ✅ The `.gitignore` file is configured to exclude `.env`
- ✅ Use environment variables instead of hardcoding keys

## 🛠️ Troubleshooting

### Common Errors

**Error: GOOGLE_API_KEY not found**
- Make sure you created a `.env` file in the project root
- Check that the key is properly formatted: `GOOGLE_API_KEY=your_key`

**429 Quota Exceeded**
- You've hit the free tier limits
- Wait a few minutes before trying again
- Consider upgrading your Google AI API plan
- Switch to `gemini-2.5-flash` for higher free tier limits

**404 Model Not Found**
- The model name may be incorrect or unavailable
- Check available models at [Google AI Studio](https://makersuite.google.com)
- Try using `gemini-pro-latest` or `gemini-flash-latest`

## 📊 API Quotas (Free Tier)

- **Gemini Pro**: 2 requests/min, 50/day
- **Gemini Flash**: 15 requests/min, 1,500/day

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🔗 Resources

- [Google AI Documentation](https://ai.google.dev/docs)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Get API Key](https://makersuite.google.com/app/apikey)

## 👨‍💻 Author

Created with ❤️ for better AI interactions

---

**Note**: This tool is designed to help you write better prompts for any AI model, not just Gemini. The enhanced prompts can be used with ChatGPT, Claude, or any other LLM!
